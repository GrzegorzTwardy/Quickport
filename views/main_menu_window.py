import json
from pathlib import Path
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt

from core.mapper.mapper_engine import MapperEngine
from salesforce_api.authenticator import Authenticator
from salesforce_api.salesforce_api import SalesforceApi
from exceptions.global_exceptions import *
from ui.ui_main_menu import Ui_MainMenu
from utils.xlsx_manager import dict_to_xlsx
from dtos.credentials import Credentials

from views.mapper_list_window import MapperListWindow
from views.profile_manager_window import ProfileManagerWindow


class MainMenuWindow(QMainWindow):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        
        self.session = AppSession()
        self.full_name = None
        self.sf_api = None
        
        # views
        self.profile_manager_window = None
        self.mapper_list_window = None
        
        # mapping config
        self.pricebook_path = None
        
        self._connect_signals()
        
    
    def test_login(self):
        pass
    
    def _connect_signals(self):
        self.session.user_logged_in.connect(self.on_login)
        self.session.user_logged_out.connect(self.on_logout)
        self.ui.mappersButton.clicked.connect(self.open_mapper_list)
        self.ui.chooseFileButton.clicked.connect(self.open_file_dialog)
        self.ui.loadToSfButton.clicked.connect(self.load_data_to_Sf)
        self.ui.profilesButton.clicked.connect(self.open_profile_manager)
    
    
    def open_profile_manager(self):
        if self.profile_manager_window is None:
            self.profile_manager_window = ProfileManagerWindow(self.session)
            self.profile_manager_window.setWindowModality(Qt.ApplicationModal)
            self.profile_manager_window.destroyed.connect(lambda: setattr(self, 'profile_manager_window', None))
            self.profile_manager_window.show()
        else:
            self.profile_manager_window.show()
            self.profile_manager_window.activateWindow()
    
    
    def on_login(self):
        if self.profile_manager_window is not None:
            self.full_name = self.profile_manager_window.full_name
            self.sf_api = self.profile_manager_window.sf_api

        self.ui.exportPricebookGroupBox.setEnabled(True)
        self.ui.mappersButton.setEnabled(True)
        
        display_name = self.full_name if self.full_name else '-none-'
        self.ui.currentUsernameLabel.setText(display_name)
        
        self.load_mappers()
    
    
    def on_logout(self):
        self.ui.exportPricebookGroupBox.setEnabled(False)
        self.ui.mappersButton.setEnabled(False)
        self.ui.currentUsernameLabel.setText('-none-')        
            
        
    def open_mapper_list(self):
        if self.mapper_list_window is None:
            self.mapper_list_window = MapperListWindow(self.session)
            self.mapper_list_window.destroyed.connect(lambda: setattr(self, 'mapper_list_window', None))
            self.mapper_list_window.show()
        else:
            self.mapper_list_window.show()
            self.mapper_list_window.activateWindow()
            
    
    def load_mappers(self):
        self.ui.mapperList.clear()
        
        for json_file in self.PATH_TO_MAPPERS.glob('*.json'):
            with open(json_file, 'r', encoding='utf-8') as mapper_file:
                mapper = json.load(mapper_file)

            mapper_name = json_file.stem
            mapper_item = QListWidgetItem(mapper_name)
            mapper_item.setData(Qt.UserRole, json_file)
            self.ui.mapperList.addItem(mapper_item)
                    
        if self.ui.mapperList.count() > 0:
            self.ui.mapperList.setCurrentRow(0)
        
        
    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            'Choose pricebook file', 
            '', 
            'Excel files (*.xlsx *.xls)'
        )
        if file_path: 
            self.ui.fileLabel.setText(f"'{Path(file_path).name}'")
            self.pricebook_path = file_path
            self.ui.loadToSfButton.setEnabled(True)
            self.ui.exportCsvButton.setEnabled(True)
            
    
    def load_data_to_Sf(self):
        current_item = self.ui.mapperList.currentItem()
        mapper_path = current_item.data(Qt.UserRole)
        errors = []
        
        if not mapper_path:
            raise FileNotFoundError('Couldn\'t load selected Mapper.')
        
        engine = MapperEngine(self.pricebook_path, mapper_path, self.session)
        prod2_df, pb_entry_df = engine.map_data()
        errors.extend(engine.execution_errors)
        
        prod_results = self.sf_api.load_product2(prod2_df, 'upsert') 

        total_success = 0
        if prod_results.get('update'):
            total_success += prod_results['update']['success']
        if prod_results.get('insert'):
            total_success += prod_results['insert']['success']
        
        if total_success > 0:
            self.sf_api.load_pricebook_entry(pb_entry_df)
            
            pb_name = self.pricebook_path.stem
            errors.extend(self.sf_api.execution_errors)
            if len(errors) > 0:
                dict_to_xlsx(errors, f'./output/invalid_data/invalid-rows-{pb_name}.xlsx', True)
        else:
            raise ProductsNotLoadedError('There were no products that could be properly loaded into Product2 object.')
        
    
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    # from PySide6.QtCore import QTimer

    app = QApplication(sys.argv)

    main_menu = MainMenuWindow()
    main_menu.show()
    
    sys.exit(app.exec())
    