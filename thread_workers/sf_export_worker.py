from pathlib import Path
from datetime import date
from PySide6.QtCore import QThread, Signal, Qt
from core.mapper.mapper_engine import MapperEngine
from core.settings.settings_manager import settings_manager
from utils.xlsx_manager import dict_to_xlsx
from dtos.session import AppSession
from salesforce_api.salesforce_api import SalesforceApi


class SalesforceExportWorker(QThread):
    
    OUTPUT_PATH = settings_manager.get_setting('output_path')
    update_label = Signal(str)
    update_progress_bar = Signal(int, int) # max_value, value
    finished_success = Signal()
    finished_warning = Signal(str)
    finished_error = Signal(str)
    
    
    def __init__(
            self, 
            mapper_path: Path, 
            pricebook_path: Path | str,
            session: AppSession,
            sf_api: SalesforceApi
        ):
        super().__init__()
        self.mapper_path = mapper_path
        self.pricebook_path = pricebook_path
        self.session = session
        self.sf_api = sf_api
        
        
    def run(self):
        errors = []
        
        try:
            self.update_label.emit('Transforming files...')
            
            engine = MapperEngine(self.pricebook_path, self.mapper_path, self.session)
            prod2_df, pb_entry_df = engine.map_data()
            errors.extend(engine.execution_errors)
            
            self.update_label.emit('Loading data to Product2 object...')
            
            prod_results = self.sf_api.load_product2(prod2_df, 'upsert') 

            total_success = 0
            if prod_results.get('update'):
                total_success += prod_results['update']['success']
            if prod_results.get('insert'):
                total_success += prod_results['insert']['success']
            
            if total_success > 0:
                
                self.update_label.emit('Loading entries to pricebooks(s)...')
                
                self.sf_api.load_pricebook_entry(pb_entry_df)
                
                pb_name = Path(self.pricebook_path).stem
                errors.extend(self.sf_api.execution_errors)
                
                if len(errors) > 0:
                    
                    self.update_label.emit('Saving faulty records...')
                    
                    # TODO: MOVE THIS TO app.py
                    Path(self.OUTPUT_PATH).mkdir(parents=True, exist_ok=True)
                    error_file = Path(self.OUTPUT_PATH) / f'{date.today().isoformat()}_{pb_name}_invalid_records.xlsx'
                    dict_to_xlsx(errors, error_file, True)
                    
                    self.update_label.emit('Finished.')
                    self.update_progress_bar.emit(1, 1)
                    self.finished_warning.emit(f'Data exported partially. Faulty records saved in file:\n{error_file}')
                else:
                    self.update_label.emit('Finished.')
                    self.update_progress_bar.emit(1, 1)
                    self.finished_success.emit()
            else:
                
                self.update_label.emit('Finished.')
                self.update_progress_bar.emit(1, 1)
                
                self.finished_error.emit('There were no products that could be properly loaded into Product2 object.')
        
        except Exception as e:
            self.finished_error.emit(str(e))