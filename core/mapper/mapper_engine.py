import json
import pandas as pd
from pathlib import Path

from core.mapper.mapper_model import MapperModel, ProductFieldMapping, PricebookConfig, CurrencyMapping
from utils.xlsx_manager import get_sheets_from_file
from core.mapper.mapper_functions import apply_mapping_function

from dtos.session import AppSession

from exceptions.mapper_exceptions import *
from exceptions.global_exceptions import *

# transformacja danych na dane zgode z obiektami Product2 i PricebookEntries w Salesforce
# TODO: mapowanie na obiekt pb-entries

class MapperEngine:

    def __init__(self, pricebook_path: Path | str, mapper_path: Path | str, session: AppSession):
        session.validate()
        self.session = session
        
        # TODO: zrobić zestaw danych opisujących 
        
        self.pricebooks: dict[str, pd.DataFrame] = get_sheets_from_file(pricebook_path)
        with open(mapper_path, 'r') as mapper_file:
            mapper_dict = json.load(mapper_file)
            self.mapper = MapperModel.from_dict(mapper_dict)
        
        self.mapped_prod2 = pd.DataFrame()
        self.mapped_entries = pd.DataFrame()
        # invalid data
        self.invalid_data = {
            'prod2-rows': [],
            'entries-rows': []
        }

        # constants
        self.product2_fields_count = len(self.mapper.sheet_rules[0].product2_mappings)


    def map_and_save(self):
        # Tymczasowo, żeby prod2 działało
        prod2 = self.map_data()[0]
        prod2_path = Path('./output/ab-renewals.csv')  
        prod2.to_csv(prod2_path, index=False)


    def map_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
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
        
        # TODO: dac ten sam error ale dla entries
        
        
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
        entries_result = pd.DataFrame()
        
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
                    
        # === MAPPPING PRICEBOOK ENTRIES ===
        # TODO WAŻNIEJSZE: czy pb_entries ma być utworzone dopiero po przesłaniu prod2
        # do Salesforce, bo pb_entries wymaga id prod2, które tworzy się na Sf
        # TODO: sprawdzić, czy oprócz pb_id, prod2_id, price coś ma być z pb_entries_fields
        for config in pb_configs:
            pb_id = config.pricebook_id
            currencies = []
            for currency_mapping in config.currencies:  
                    pass
            
        return prod2_result, entries_result


    def _collect_invalid_rows(
        self,
        sheet_df: pd.DataFrame,
        invalid_mask: pd.Series,
        sheet_name: str,
        sf_field: str,
        reason: str
    ):
        invalid_rows = sheet_df.loc[invalid_mask]
        for idx, row in invalid_rows.iterrows():
            self.invalid_data['prod2-rows'].append({
                'sheet': sheet_name,
                'field': sf_field,
                'reason': reason,
                'msg': f'Invalid data in sheet "{sheet_name}", row "{idx}". Reason: "{reason}"',
                'row': row
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

    prod2 = engine.map_and_save()
    for pdr in engine.invalid_data['prod2-rows']:
        print(pdr['msg'])
    # print(len(engine.invalid_data['prod2-rows']))