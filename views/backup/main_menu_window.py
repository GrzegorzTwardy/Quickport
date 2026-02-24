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


class MainMenuWindow(QMainWindow):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    CLIENT_ID = '3MVG9YFqzc_KnL.zP4xDXrq_EmgXWyf0hdCUgCi1fEcFg.GDfYOIC__TDQmQIRDjOMay96.sWNCCKkiq2ECIJ'
    # CLIENT_ID = '3MVG9YFqzc_KnL.zxPe.IGRlPbs_tOBWClS08_uAIV7Jvp8DpFZvnUgGeys2v_Mu.PN3Cr51zohuqk2cBSmRR'
    # cliend id = consumer key
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        
        self.session = AppSession()
        self.full_name = None
        self.sf_api = None
        
        # views
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
        self.ui.loginButton.clicked.connect(self.login)
    
        
    def on_login(self):
        self.ui.exportPricebookGroupBox.setEnabled(True)
        self.ui.mappersButton.setEnabled(True)
        self.ui.currentUsernameLabel.setText(self.full_name)
        
        self.load_mappers()

    
    def on_logout(self):
        self.ui.exportPricebookGroupBox.setEnabled(False)
        self.ui.mappersButton.setEnabled(False)
        self.ui.currentUsernameLabel.setText('-none-')
        
    
    def handle_login_success(self, token_response):
        
        def validate_metadata(sf_metadata: SfMetadata):
            errors_msgs = []

            if len(sf_metadata.available_currencies) == 0:
                errors_msgs.append('avaliable currencies')
            if len(sf_metadata.pricebooks) == 0:
                errors_msgs.append('pricebooks')
            if len(sf_metadata.product2_fields) == 0:
                errors_msgs.append('Product2 fields')
            elif 'ProductCode' not in sf_metadata.product2_fields:
                errors_msgs.append("'ProductCode' field in Product2 object (obligatory field)")
                
            if errors_msgs:
                msg = 'This account does not have/is missing required data:\n'
                for m in errors_msgs:
                    msg += f"- {m}\n"
                
                raise ValueError(msg.rstrip())
        
        try:
            self.full_name = Authenticator.get_user_display_name(
                identity_url=token_response['id'], 
                access_token=token_response['access_token']
            )

            creds = Credentials(
                access_token=token_response['access_token'],
                refresh_token=token_response.get('refresh_token'),
                instance_url=token_response['instance_url'],
                client_id=self.CLIENT_ID
            )

            self.sf_api = SalesforceApi(creds=creds)

            sf_metadata = self.sf_api.get_user_sf_metadata()
            
            # validate user's Salesforce info
            validate_metadata(sf_metadata)

            self.session.login(sf_metadata)
            
            self.ui.loginButton.setText('Re-login')
            self.ui.loginButton.setEnabled(True)
            
            QMessageBox.information(self, "Success", f"Successfully logged as:\n{self.full_name}")
        except Exception as e:
            self.handle_login_error(str(e))
    
    
    def handle_login_error(self, error_message):
        self.ui.loginButton.setEnabled(True)
        self.ui.loginButton.setText("Login")
        
        if "has been canceled" not in error_message:
            QMessageBox.critical(self, "Authorization Error", f"Error:\n{error_message}")


    def login(self):
        if hasattr(self, 'auth_thread') and self.auth_thread.isRunning():
            self.auth_thread.cancel()
            self.ui.loginButton.setEnabled(False)
            self.ui.loginButton.setText("Cancelling...")
            return
        
        if self.ui.logToSandbox.isChecked():
            login_url = "https://test.salesforce.com"
        else:
            login_url = "https://login.salesforce.com"
            
        self.ui.loginButton.setEnabled(True)
        self.ui.loginButton.setText("Cancel")
        
        # using "self." so it doesn't end up in the garbage collector
        self.auth_thread = Authenticator(
            client_id=self.CLIENT_ID,
            login_url=login_url
        )
        
        self.auth_thread.login_successful.connect(self.handle_login_success)
        self.auth_thread.login_failed.connect(self.handle_login_error)

        self.auth_thread.start()        
            
        
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