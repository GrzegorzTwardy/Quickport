import time
import logging
import requests
import numpy as np
import pandas as pd
from pathlib import Path
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from core.profile.profile_model import Profile
from requests.exceptions import RequestException
from simple_salesforce import Salesforce
from exceptions.sf_api_exceptions import *


class SalesforceApi:
    
    def __init__(self, profile: Profile):
        self.sf = None
        self.username = profile.uname
        self.password = profile.password
        self.security_token = profile.security_token
        self.consumer_key = profile.consumer_key
        self.consumer_secret = profile.consumer_secret
        self.instance_url = profile.instance_url

        # logger
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # SF Objects
        self.standard_pricebook_dict = {} # id: name
        self.custom_pricebooks_dict = {} # id: name
        
        
        self.connect()
        self.load_all_pricebooks()


    def connect(self) -> Salesforce:
        url = f'{self.instance_url}/services/oauth2/token'

        data = {
            'grant_type': 'password',
            'client_id': self.consumer_key,
            'client_secret': self.consumer_secret,
            'username': self.username,
            'password': f'{self.password}{self.security_token}',
        }

        try:
            response = requests.post(url, data=data, timeout=15)
            response.raise_for_status() # !200 => exception
            payload = response.json()

            if 'access_token' not in payload or 'instance_url' not in payload:
                raise ValueError(f'Invalid OAuth response: {payload}')

            token = payload['access_token']
            instance = payload['instance_url']

            self.sf = Salesforce(instance_url=instance, session_id=token)
            print('Connection with Salesforce established.')
            
        except RequestException as e:
            print('Error: Couldn\'t connect with Salesforce API.')
            print(str(e))
            raise
        except ValueError as e:
            print('Error: Invalid server response.')
            print(str(e))
            raise
        except Exception as e:
            print('Unexpected Error.')
            print(str(e))
            raise

    
    # === fetching data for mappers === 
    def get_prod2_fields(self):
        desc = self.sf.Product2.describe()
        field_names = [f['name'] for f in desc['fields'] if f['name'] != 'Id']
        return field_names
    
    
    def get_pb_entry_fields(self):
        desc = self.sf.PricebookEntry.describe()
        field_names = [f['name'] for f in desc['fields'] if f['name'] != 'Id']
        return field_names
    
    
    def load_all_pricebooks(self):
        # custom pricebooks (Pricebook2)
        custom_records = self.sf.query_all("""
            SELECT Id, Name
            FROM Pricebook2
            WHERE IsActive = true
            AND IsStandard = false
            ORDER BY Name ASC
        """) 
        self.custom_pricebooks_dict = { row['Id']: row['Name'] for row in custom_records['records'] } 
        
        # Standard Pricebook
        standard_records = self.sf.query("""
            SELECT Id, Name
            FROM Pricebook2
            WHERE IsStandard = true
        """)
        self.standard_pricebook_dict = {
            row['Id']: row['Name'] for row in standard_records['records'] 
        }
        print('Pricebooks loaded.')
    
    
    def get_available_currencies(self):
        result = self.sf.query("SELECT IsoCode FROM CurrencyType WHERE IsActive = true")
        return [row["IsoCode"] for row in result["records"]]


    def get_mappable_object_fields(self, object_name: str) -> dict[str, dict]:
        desc = getattr(self.sf, object_name).describe()
        result: dict[str, dict] = {}

        for field in desc['fields']:
            name = field['name']

            # === HARD FILTERS ===
            if name == 'Id':
                continue
            if field.get('calculated'):
                continue
            if not field.get('createable'):
                continue
            if not field.get('updateable'):
                continue
            if field.get('autoNumber'):
                continue
            if field.get('deprecatedAndHidden'):
                continue
            # if field.get('type') in {'address', 'location', 'base64'}:
            #     continue

            # === BUILD UI METADATA ===
            result[name] = {
                'label': field.get('label'),
                'type': field.get('type'),
                'required': not field.get('nillable', True),
                'nillable': field.get('nillable', True),
                'defaultedOnCreate': field.get('defaultedOnCreate', False),
                'length': field.get('length'),
                'precision': field.get('precision'),
                'scale': field.get('scale'),
                'picklistValues': [
                    pv['value']
                    for pv in field.get('picklistValues', [])
                    if pv.get('active')
                ],
                'referenceTo': field.get('referenceTo', []),
            }

        return result

    
    def get_user_sf_metadata(self) -> SfMetadata:   
        return SfMetadata(
            product2_fields=self.get_mappable_object_fields('Product2'),
            pb_entries_fields=self.get_mappable_object_fields('PricebookEntry'),
            pricebooks=self.custom_pricebooks_dict,
            available_currencies=self.get_available_currencies()
        )
        
    
    def load_product2_to_Sf(
        self,
        file_path: Path | str,
        operation: str,
        batch_size: int = 5000
    ):
        try:
            self.logger.info("Start loading Product2 to Salesforce")
            self.logger.info(f"File: {file_path}, operation: {operation}")

            # ========================
            # 1. Validate CSV columns
            # ========================
            self.logger.info("Validating CSV columns...")

            allowed_api_names = self.get_prod2_fields()
            df = pd.read_csv(file_path)
            csv_columns = df.columns.tolist()

            invalid = [col for col in csv_columns if col not in allowed_api_names]
            if invalid:
                raise InvalidCsvColumnNamesError(invalid, "Product2")

            self.logger.info("CSV validation passed")
            
            
            # ========================
            # 2. Load data using Bulk API v1
            # ========================
            self.logger.info("Sending data to Salesforce (Bulk API v1)...")
            
            df = df.astype(object)
            df = df.replace([np.inf, -np.inf, np.nan], None)
            df = df.where(pd.notna(df), None) # sanitize NaN
            records = df.to_dict(orient="records")

            bulk_obj = self.sf.bulk.Product2

            if operation == "insert":
                result = bulk_obj.insert(records, batch_size=batch_size)
            elif operation == "update":
                result = bulk_obj.update(records, batch_size=batch_size)
            elif operation == "upsert":
                result = bulk_obj.upsert(
                    records,
                    external_id_field="ProductCode",
                    batch_size=batch_size
                )
            elif operation == "delete":
                result = bulk_obj.delete(records, batch_size=batch_size)
            else:
                raise ValueError(f"Unsupported operation: {operation}")

            # ========================
            # 3. Analyze results
            # ========================
            success = sum(1 for r in result if r.get("success"))
            failed = len(result) - success

            self.logger.info(f"✔️ Success: {success}")
            self.logger.info(f"❌ Failed: {failed}")

            if failed:
                errors = [r for r in result if not r.get("success")]
                self.logger.error(f"Errors: {errors[:5]}")  # pokaz pierwsze 5

            return {
                "success": success,
                "failed": failed,
                "total": len(result)
            }

        except Exception:
            self.logger.exception("❌ Error while loading Product2")
            raise


    
if __name__ == '__main__':
    profile = Profile.from_json('./cert/test_creds.json')    
    api = SalesforceApi(profile)
    meta = api.get_user_sf_metadata()
    print(meta.product2_fields.items())
    # api.load_product2_to_Sf('./output/ab-renewals.csv', 'insert')
    # print(api.custom_pricebooks_dict)
    # print(api.standard_pricebook_dict)