from pathlib import Path
from datetime import datetime
from PySide6.QtCore import QThread, Signal, Qt
from core.mapper.mapper_engine import MapperEngine
from core.settings.settings_manager import settings_manager
from utils.xlsx_manager import dict_to_xlsx
from dtos.session import AppSession


class CsvExportWorker(QThread):
    
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
        ):
        super().__init__()
        self.mapper_path = mapper_path
        self.pricebook_path = pricebook_path
        self.session = session
        
    
    @property
    def output_path(self):
        return settings_manager.get_setting('output_path')
    
        
    def run(self):
        errors = []
        
        try:
            self.update_label.emit('Transforming files...')
            
            engine = MapperEngine(self.pricebook_path, self.mapper_path, self.session)
            prod2_df, pb_entry_df = engine.map_data()
            errors.extend(engine.execution_errors)
            
            pb_name = Path(self.pricebook_path).stem
            
            self.update_label.emit('Saving Product2 and PricebookEntry files...')
            
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_folder_path = Path(self.output_path) / f'{timestamp}_{pb_name}'
            output_folder_path.mkdir(parents=True, exist_ok=True)
            
            prod2_file_path = output_folder_path / f'{timestamp}_{pb_name}_product2.csv'
            pb_entry_file_path = output_folder_path / f'{timestamp}_{pb_name}_pricebook_entry.csv'
            
            prod2_df.to_csv(prod2_file_path, index=False)
            pb_entry_df.to_csv(pb_entry_file_path, index=False)
            
            if len(errors) > 0:
                
                self.update_label.emit('Saving faulty records...')
                
                error_file = output_folder_path / f'{timestamp}_{pb_name}_invalid_records.xlsx'
                dict_to_xlsx(errors, error_file, True)
                
                self.update_label.emit('Finished.')
                self.update_progress_bar.emit(1, 1)
                self.finished_warning.emit(f'Data was exported partially. Faulty records have been saved in file:\n{error_file}')
            else:
                self.update_label.emit('Finished.')
                self.update_progress_bar.emit(1, 1)
                self.finished_success.emit()
        
        except Exception as e:
            self.finished_error.emit(str(e))