import time
import json
import pandas as pd
from pathlib import Path

from core.mapper.mapper_model import MapperModel, ProductFieldMapping, PricebookConfig, CurrencyMapping
from utils.xlsx_manager import get_sheets_from_file
from core.mapper.mapper_functions import apply_mapping_function

from dtos.session import AppSession

from exceptions.mapper_exceptions import *
from exceptions.global_exceptions import *

# transformacja danych na dane zgodne z obiektami Product2 i PricebookEntry w Salesforce
# WAŻNE: zakładamy, że pole ProductCode jest wymaganym i unikalnym polem obiektu w Salesforce
# i na jego podstawie działają poniższe funkcje - brak tego pola skutuje błędem

class MapperEngine:

    def __init__(self, pricebook_path: Path | str, mapper_path: Path | str, session: AppSession):
        session.validate()
        self.session = session
        
        self.pricebooks: dict[str, pd.DataFrame] = get_sheets_from_file(pricebook_path)
        with open(mapper_path, 'r') as mapper_file:
            mapper_dict = json.load(mapper_file)
            self.mapper = MapperModel.from_dict(mapper_dict)
        
        self.mapped_prod2 = pd.DataFrame()
        self.mapped_entries = pd.DataFrame()

        self.execution_errors = [] # Format: [{'Source': str, 'Message': str, 'Details': str}]
        
        # for map_and_save()
        self.pricebook_name = Path(pricebook_path).stem
        self.mapper_name = Path(mapper_path).stem


    # .csv ==> Product2 df and PricebookEntry df
    def map_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.execution_errors = []
        
        all_prod2_headers = set()
        all_pb_entries_headers = self.session.sf_metadata.pb_entries_fields

        for sheet_rule in self.mapper.sheet_rules:
            for mapping in sheet_rule.product2_mappings:
                all_prod2_headers.add(mapping.sf_target_field)
        
        # Product2 object table
        prod2_df = pd.DataFrame(columns=list(all_prod2_headers))
        prod2_frames = []
        # PricebookEntries object table
        entries_df = pd.DataFrame(columns=list(all_pb_entries_headers))
        entries_df_frames = []
        
        for sheet_rule in self.mapper.sheet_rules:
            pb_name = sheet_rule.sheet_name
            
            if pb_name not in self.pricebooks:
                raise SheetNotFoundError(f'Sheet "{pb_name}" has not been found')
            sheet = self.pricebooks[pb_name]
            
            prod2_sheet_df, entries_sheet_df = self.map_sheet(
                sheet_df=sheet,
                sheet_name=pb_name, # for info in errors
                prod2_mappings=sheet_rule.product2_mappings,
                pb_configs=sheet_rule.pricebook_configs
            )
            
            prod2_frames.append(prod2_sheet_df)
            entries_df_frames.append(entries_sheet_df)
            
        
        if not prod2_frames:
            raise MappingError('No product mappings defined')
        
        if not entries_df_frames:
            raise MappingError('There was no currency and price configuration for any pricebook')
        
        
        prod2_df = pd.concat(prod2_frames) # ready prod2 data
        entries_df = pd.concat(entries_df_frames)   
        
        return prod2_df, entries_df 

                
    def map_sheet(
            self,
            sheet_df: pd.DataFrame,
            sheet_name: str, # for info in errors
            prod2_mappings: list[ProductFieldMapping],
            pb_configs: list[PricebookConfig]
        ) -> tuple[pd.DataFrame, pd.DataFrame]:
        
        def raw_column(column: pd.Series):
            values = column.copy()
            invalid_mask = values.isna()
            return values, invalid_mask
                
        prod2_result = pd.DataFrame(index=sheet_df.index)
        
        # === MAPPING PROD2 FIELDS ===
        for mapping in prod2_mappings:
            
            sf_field = mapping.sf_target_field
            
            # validating mapper data with sf_metadata
            if sf_field not in self.session.sf_metadata.product2_fields:
                raise TargetSfFieldNotFoundError(
                    f'Mapper file defines Salesforce object\'s field "{sf_field}" that doesn\'t exist in Salesforce.'
                )
            
            if not mapping.included:
                prod2_result[sf_field] = None
                continue
            
            # raw column
            if mapping.source_column:
                if mapping.source_column not in sheet_df.columns:
                    raise SourceColumnNotFoundError(
                        f"""Column "{mapping.source_column}" not found in sheet "{sheet_name}".
                        (mapping to SF field "{sf_field}")"""
                    )
                
                values, invalid_mask = raw_column(sheet_df[mapping.source_column])
            # mapping
            elif mapping.mapping_type:
                values, invalid_mask = apply_mapping_function(sheet_df, mapping)  

            
            prod2_result[sf_field] = values

            # ---- mapping function errors
            if mapping.mapping_type and invalid_mask.any():
                self._collect_invalid_rows(
                    sheet_df,
                    invalid_mask,
                    sheet_name,
                    sf_field,
                    reason=f'Mapping type {mapping.mapping_type} failed'
                )
            
            # ---- handling unwanted nulls
            if not mapping.allows_nulls:
                null_mask = values.isna()

                if null_mask.any():
                    self._collect_invalid_rows(
                        sheet_df,
                        null_mask,
                        sheet_name,
                        sf_field,
                        reason='Null value not allowed'
                    )
        
        # check if ProductCode (key field for mapping PricebookEntry) is missing
        if 'ProductCode' not in prod2_result.columns:
            raise MappingError(f'ProductCode is missing in sheet {sheet_name}')
        if prod2_result['ProductCode'].isna().all():
            raise MappingError(f'ProductCode is required in sheet {sheet_name}')
        
        
        # === MAPPPING PRICEBOOKENTRY ===
        entries_frames = []
        sku_series = prod2_result['ProductCode']

        for pb_config in pb_configs:
            for currency in pb_config.currencies:
                source_col = currency.source_column
                
                if source_col not in sheet_df.columns:
                    raise SourceColumnNotFoundError(
                        f"""Column "{source_col}" not found in sheet "{sheet_name}".
                            (while configuring currencies in pricebooks)"""
                    )

                temp_df = pd.DataFrame({
                    'ProductCode': sku_series,
                    'raw_price': sheet_df[source_col]
                })

                # removing missing skus and prices
                temp_df = temp_df.dropna(subset=['ProductCode', 'raw_price'])
                
                if temp_df.empty:
                    continue

                temp_df['Pricebook2Id'] = pb_config.pricebook_id
                temp_df['CurrencyIsoCode'] = currency.code
                temp_df['UnitPrice'] = temp_df['raw_price'] * currency.conversion_factor
                temp_df['IsActive'] = True

                final_cols = ['ProductCode', 'Pricebook2Id', 'CurrencyIsoCode', 'UnitPrice', 'IsActive']
                entries_frames.append(temp_df[final_cols])

        if entries_frames:
            entries_result = pd.concat(entries_frames, ignore_index=True)
        else:
            entries_result = pd.DataFrame(columns=['ProductCode', 'Pricebook2Id', 'CurrencyIsoCode', 'UnitPrice', 'IsActive'])

        return prod2_result, entries_result


    def _collect_invalid_rows(
        self,
        sheet_df: pd.DataFrame,
        invalid_mask: pd.Series,
        sheet_name: str,
        message: str
    ):
        invalid_rows = sheet_df.loc[invalid_mask]
        for idx, row in invalid_rows.iterrows():
            row_dict = row.to_dict()
            row_clean = {k: v for k, v in row_dict.items() if pd.notna(v)}
            
            self.execution_errors.append({
                'Source': f'Mapper: {sheet_name}',
                'Message': message,
                'Details': f'Row {idx}: {str(row_clean)}'
            })
    

if __name__ == '__main__':
    from core.profile.profile_model import Profile
    from salesforce_api.salesforce_api import SalesforceApi
    
    pb_path = Path('./data/ab.xlsx')
    m_path = Path('./mappers/ab-mapper.json')
    
    profile = Profile.from_json('./cert/test_creds.json')    
    sf_api = SalesforceApi(profile)
    sf_api.connect()

    session = AppSession()
    session.login(
        user_id='123213', 
        sf_metadata=sf_api.get_user_sf_metadata()
    )
    
    engine = MapperEngine(pb_path, m_path, session)
    engine.map_and_save()