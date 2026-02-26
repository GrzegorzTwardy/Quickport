import io
import time
import logging
import requests
import pandas as pd
from pathlib import Path
from functools import wraps
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from dtos.credentials import Credentials
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceExpiredSession
from exceptions.sf_api_exceptions import *


def auto_refresh_token(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        
        except SalesforceExpiredSession:
            self.logger.warning(f"Session expried while invoking '{func.__name__}'. Refreshing tokens...")
            self._refresh_access_token()
            
            self.sf = Salesforce(
                instance_url=self.instance_url, 
                session_id=self.access_token
            )
            
            self.logger.info("Retrying request...")
            return func(self, *args, **kwargs)
    
    return wrapper


class SalesforceApi:
    
    def __init__(self, creds: Credentials):
        self.sf = None

        self.access_token = creds.access_token
        self.refresh_token = creds.refresh_token
        self.instance_url = creds.instance_url
        self.client_id = creds.client_id

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        self.standard_pricebook_dict = {} 
        self.custom_pricebooks_dict = {} 
        self.execution_errors = [] 
        
        self.connect()
        self.load_all_pricebooks()
        

    @auto_refresh_token
    def connect(self) -> Salesforce:
        try:
            self.sf = Salesforce(
                instance_url=self.instance_url, 
                session_id=self.access_token
            )
            self.sf.limits()
            self.logger.info('Połączenie z Salesforce ustanowione (Access Token aktywny).')   
        except Exception as e:
            self.logger.error(e)

    
    def _refresh_access_token(self):
        if not self.refresh_token:
            raise ValueError("Brak Refresh Tokena. Użytkownik musi zalogować się ponownie.")

        token_url = f'{self.instance_url}/services/oauth2/token'
        
        data = {
            'grant_type': 'refresh_token',
            'client_id': self.consumer_key,
            'refresh_token': self.refresh_token
        }

        response = requests.post(token_url, data=data, timeout=15)
        
        if response.status_code != 200:
            self.logger.error(f"Nie udało się odświeżyć tokena: {response.text}")
            raise ConnectionError("Refresh token wygasł lub jest nieprawidłowy. Wymagane ponowne logowanie w przeglądarce.")
            
        payload = response.json()
        self.access_token = payload['access_token']
        
        self.logger.info("Access Token został pomyślnie odświeżony.")


    # === Metadata Helpers === 
    @auto_refresh_token
    def get_prod2_fields(self):
        desc = self.sf.Product2.describe()
        return [f['name'] for f in desc['fields'] if f['name'] != 'Id']
    
    
    @auto_refresh_token
    def get_pb_entry_fields(self):
        desc = self.sf.PricebookEntry.describe()
        return [f['name'] for f in desc['fields'] if f['name'] != 'Id']
    
    
    @auto_refresh_token
    def load_all_pricebooks(self):
        try:
            custom_records = self.sf.query_all("SELECT Id, Name FROM Pricebook2 WHERE IsActive = true AND IsStandard = false ORDER BY Name ASC") 
            self.custom_pricebooks_dict = {row['Id']: row['Name'] for row in custom_records['records']} 
            
            standard_records = self.sf.query("SELECT Id, Name FROM Pricebook2 WHERE IsStandard = true")
            self.standard_pricebook_dict = {row['Id']: row['Name'] for row in standard_records['records']}
            self.logger.info('Pricebooks loaded.')
        except Exception as e:
            self._register_error("Metadata", f"Failed to load pricebooks: {e}")


    @auto_refresh_token
    def get_available_currencies(self):
        try:
            result = self.sf.query("SELECT IsoCode FROM CurrencyType WHERE IsActive = true")
            return [row["IsoCode"] for row in result["records"]]
        except Exception:
            return []


    @auto_refresh_token
    def get_mappable_object_fields(self, object_name: str) -> dict[str, dict]:
        desc = getattr(self.sf, object_name).describe()
        result: dict[str, dict] = {}
        for field in desc['fields']:
            name = field['name']
            if name == 'Id' or field.get('calculated') or not field.get('createable') or field.get('autoNumber'):
                continue
            
            result[name] = {
                'label': field.get('label'),
                'type': field.get('type'),
                'required': not field.get('nillable', True),
                'picklistValues': [pv['value'] for pv in field.get('picklistValues', []) if pv.get('active')]
            }
        return result
    
    @auto_refresh_token
    def get_user_sf_metadata(self) -> SfMetadata:   
        return SfMetadata(
            product2_fields=self.get_mappable_object_fields('Product2'),
            pb_entries_fields=self.get_mappable_object_fields('PricebookEntry'),
            pricebooks=self.custom_pricebooks_dict,
            available_currencies=self.get_available_currencies()
        )

    # === ERROR HANDLING & HELPERS ===
    def _register_error(self, source: str, message: str, details: str = ""):
        self.execution_errors.append({
            "Source": source,
            "Message": message,
            "Details": details
        })

    def _parse_and_register_bulk_errors(self, job_context: str, error_csv: str):
        if not error_csv: return
        try:
            df_err = pd.read_csv(io.StringIO(error_csv))
            for _, row in df_err.iterrows():
                error_msg = row.get("sf__Error", "Unknown Error")
                record_data = row.drop(["sf__Id", "sf__Error"], errors='ignore').to_dict()
                
                self._register_error(
                    source=f"API Bulk: {job_context}",
                    message=error_msg,
                    details=str(record_data)
                )
        except Exception as e:
            self.logger.error(f"Failed to parse error CSV: {e}")


    @auto_refresh_token
    def _get_product_id_map(self, skus: list) -> dict:
        if not skus: return {}
        sku_strings = "'" + "','".join([str(s).replace("'", "\\'") for s in skus]) + "'"
        query = f"SELECT Id, ProductCode FROM Product2 WHERE ProductCode IN ({sku_strings})"
        
        self.logger.info(f"Fetching Product2 mapping for {len(skus)} SKUs...")
        res = self.sf.query_all(query)
        return {row['ProductCode']: row['Id'] for row in res['records'] if row['ProductCode']}

    @auto_refresh_token
    def _get_existing_pbe_map(self, product_ids: list) -> dict:
        if not product_ids: return {}
        
        self.logger.info(f"Fetching existing PricebookEntries for {len(product_ids)} products...")
        p_ids_str = "'" + "','".join(product_ids) + "'"
        query = f"SELECT Id, Product2Id, Pricebook2Id, CurrencyIsoCode FROM PricebookEntry WHERE Product2Id IN ({p_ids_str})"
        
        res = self.sf.query_all(query)
        mapping = {}
        for row in res['records']:
            key = (row['Product2Id'], row['Pricebook2Id'], row['CurrencyIsoCode'])
            mapping[key] = row['Id']
        return mapping


    # === Bulk Jobs ===
    @auto_refresh_token
    def _execute_bulk_v2(self, df: pd.DataFrame, object_name: str, operation: str, poll_interval: int = 2):
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False, lineterminator='\n')
        
        base_url = self.sf.base_url if self.sf.base_url.endswith('/') else f"{self.sf.base_url}/"
        job_url = f"{base_url}jobs/ingest"
        headers = {
            'Authorization': f'Bearer {self.sf.session_id}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        job_payload = {"object": object_name, "operation": operation, "lineEnding": "LF"}
        
        resp = self.sf.session.post(job_url, json=job_payload, headers=headers)
        if resp.status_code != 200:
            err_msg = f"Failed to create job: {resp.text}"
            self._register_error(f"Setup {object_name}", err_msg)
            raise SalesforceApiError(err_msg)
        
        job_id = resp.json()['id']
        
        upload_url = f"{job_url}/{job_id}/batches"
        csv_headers = headers.copy()
        csv_headers['Content-Type'] = 'text/csv'
        self.sf.session.put(upload_url, data=csv_buffer.getvalue().encode('utf-8'), headers=csv_headers).raise_for_status()

        self.sf.session.patch(f"{job_url}/{job_id}/", json={'state': 'UploadComplete'}, headers=headers).raise_for_status()

        while True:
            status_res = self.sf.session.get(f"{job_url}/{job_id}/", headers=headers).json()
            state = status_res['state']
            if state in ['Failed', 'Aborted']:
                err_msg = status_res.get('errorMessage', 'Unknown fatal error')
                self._register_error(f"Job {object_name}", err_msg)
                raise SalesforceJobFailedError(err_msg)
            if state == 'JobComplete':
                break
            time.sleep(poll_interval)

        processed = status_res.get('numberRecordsProcessed', 0)
        failed_count = status_res.get('numberRecordsFailed', 0)
        
        results = {"success": processed - failed_count, "failed": failed_count}

        if failed_count > 0:
            failed_res = self.sf.session.get(f"{job_url}/{job_id}/failedResults/", headers=headers)
            self._parse_and_register_bulk_errors(f"{object_name} {operation}", failed_res.text)
            self.logger.warning(f"Bulk Job {job_id} finished with errors. Failed: {failed_count}")

        return results


    # === LOAD METHODS ===

    # == Product2 ===
    @auto_refresh_token
    def load_product2(self, data: pd.DataFrame | str | Path, operation: str = 'upsert', poll_interval: int = 2):
        self.logger.info("Start loading Product2...")
        # self.execution_errors = [] 
        
        if isinstance(data, (str, Path)):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            self._register_error("Load Product2", "Invalid data format")
            return {"update": None, "insert": None}

        if "ProductCode" not in df.columns:
            self._register_error("Load Product2", "Missing ProductCode column")
            raise MissingRequiredColumnError("ProductCode is required.")

        try:
            skus_in_file = df['ProductCode'].dropna().unique().tolist()
            prod_map = self._get_product_id_map(skus_in_file)
        except Exception as e:
            self._register_error("Load Product2", f"Failed to fetch metadata: {e}")
            raise

        df['Id'] = df['ProductCode'].map(prod_map)
        
        df_update = df[df['Id'].notna()].copy()
        df_insert = df[df['Id'].isna()].drop(columns=['Id'])

        results = {"update": None, "insert": None}

        if not df_update.empty:
            results["update"] = self._execute_bulk_v2(df_update, "Product2", "update", poll_interval)
        if not df_insert.empty:
            results["insert"] = self._execute_bulk_v2(df_insert, "Product2", "insert", poll_interval)

        return results

    # == PricebookEntry ===
    @auto_refresh_token
    def load_pricebook_entry(self, data: pd.DataFrame | str | Path, poll_interval: int = 2):
        self.logger.info("Start synchronizing PricebookEntries...")
        
        if isinstance(data, (str, Path)):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            self._register_error("Load Pricebooks", "Invalid data format")
            return {}

        try:
            skus_in_file = df['ProductCode'].dropna().unique().tolist()
            prod_map = self._get_product_id_map(skus_in_file)
            
            valid_product_ids = list(set([prod_map[sku] for sku in skus_in_file if sku in prod_map]))
            existing_pbe_map = self._get_existing_pbe_map(valid_product_ids)
        except Exception as e:
            self._register_error("Load Pricebooks", f"Failed to fetch metadata: {e}")
            raise

        std_pb_id = None
        for pid, name in self.standard_pricebook_dict.items():
             if 'Standard' in name or 'Standard Price Book' in name:
                 std_pb_id = pid
                 break
        if not std_pb_id:
             try:
                res = self.sf.query("SELECT Id FROM Pricebook2 WHERE IsStandard=true LIMIT 1")
                if res['totalSize'] > 0: std_pb_id = res['records'][0]['Id']
             except Exception: pass

        inserts_std, updates_std = [], []
        inserts_custom, updates_custom = [], []
        queued_std_keys = set()
        queued_std_update_keys = set()
        
        for _, row in df.iterrows():
            sku = row.get('ProductCode')
            pb_id = row.get('Pricebook2Id')
            currency = row.get('CurrencyIsoCode')
            price = row.get('UnitPrice')
            is_active = row.get('IsActive', True)

            if sku not in prod_map:
                self._register_error("Pre-check PBE", f"SKU not found in Salesforce: {sku}", str(row.to_dict()))
                continue
            
            if not pb_id or pd.isna(pb_id):
                self._register_error("Pre-check PBE", f"Missing Pricebook2Id", str(row.to_dict()))
                continue

            prod_id = prod_map[sku]
            current_comp_key = (prod_id, pb_id, currency)
            
            if std_pb_id and pb_id != std_pb_id:
                std_comp_key = (prod_id, std_pb_id, currency)
                if std_comp_key not in existing_pbe_map and std_comp_key not in queued_std_keys:
                    inserts_std.append({
                        "Pricebook2Id": std_pb_id,
                        "Product2Id": prod_id,
                        "CurrencyIsoCode": currency,
                        "UnitPrice": price,
                        "IsActive": True
                    })
                    queued_std_keys.add(std_comp_key)
                elif std_comp_key in existing_pbe_map and std_comp_key not in queued_std_update_keys:
                    updates_std.append({
                        "Id": existing_pbe_map[std_comp_key],
                        "UnitPrice": price,
                        "IsActive": is_active
                    })
                    queued_std_update_keys.add(std_comp_key)

            # Pełny rekord - przyda się do INSERTU
            insert_record = {
                "Pricebook2Id": pb_id,
                "Product2Id": prod_id,
                "CurrencyIsoCode": currency,
                "UnitPrice": price,
                "IsActive": is_active
            }
            
            # Ograniczony rekord - TYLKO DO UPDATE'U (usunięto zablokowane pola)
            update_record = {
                "UnitPrice": price,
                "IsActive": is_active
            }

            is_target_std = (pb_id == std_pb_id)

            if current_comp_key in existing_pbe_map:
                # Jeśli rekord istnieje - dodajemy ID do przygotowanego wcześniej słownika 'update_record'
                update_record['Id'] = existing_pbe_map[current_comp_key]
                if is_target_std:
                    if current_comp_key not in queued_std_update_keys:
                        updates_std.append(update_record)
                else: 
                    updates_custom.append(update_record)
            else:
                # Jeśli rekord nie istnieje - dodajemy przygotowany wcześniej słownik 'insert_record'
                if is_target_std:
                    if current_comp_key not in queued_std_keys:
                        inserts_std.append(insert_record)
                else: 
                    inserts_custom.append(insert_record)

        # Inicjujemy results żeby uniknąć zwracania pustego słownika przy błędach
        results = {"success": 0, "failed": 0} 

        # === Zapis do Salesforce ===
        # Zbiorcze wywoływanie dla estetyki logowania i uproszczenia
        def execute_job(data_list, obj_name, op_type):
            if not data_list: return
            res = self._execute_bulk_v2(pd.DataFrame(data_list), obj_name, op_type, poll_interval)
            results["success"] += res.get("success", 0)
            results["failed"] += res.get("failed", 0)

        execute_job(inserts_std, "PricebookEntry", "insert")
        execute_job(updates_std, "PricebookEntry", "update")
        execute_job(inserts_custom, "PricebookEntry", "insert")
        execute_job(updates_custom, "PricebookEntry", "update")
            
        return results
    
    
if __name__ == '__main__':
    pass