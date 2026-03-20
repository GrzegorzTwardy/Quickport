import json
from pathlib import Path
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt, Slot

from salesforce_api.authenticator import Authenticator
from salesforce_api.salesforce_api import SalesforceApi
from exceptions.global_exceptions import *
from ui.ui_main_menu import Ui_MainMenu
from utils.xlsx_manager import dict_to_xlsx
from dtos.credentials import Credentials

from views.mapper_list_window import MapperListWindow
from views.profile_manager_window import ProfileManagerWindow
from views.widgets.progress_bar_dialog import ProgressBarDialog
from utils.message_handler import MessageHandler
from thread_workers.sf_export_worker import SalesforceExportWorker


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
        if not current_item:
            return
        
        mapper_path = current_item.data(Qt.UserRole)
        if not mapper_path:
            MessageHandler.show_error(
                self,
                'Path Error',
                'Couldn\'t load selected Mapper.'
            )
            return
        
        self.progress_dialog = ProgressBarDialog('Setting up export...')
        self.progress_dialog.show()
        
        self.worker = SalesforceExportWorker(
            mapper_path=mapper_path,
            pricebook_path=self.pricebook_path,
            session=self.session,
            sf_api=self.sf_api
        )
        
        self.worker.update_label.connect(self.update_label)
        self.worker.update_progress_bar.connect(self.update_progress_bar)
        self.worker.finished_success.connect(self.diplay_success_msg)
        self.worker.finished_error.connect(self.display_failure_msg)
        self.worker.finished_warning.connect(self.display_warning_msg)
        
        self.worker.start()
        
    
    # === WORKER SINGAL SLOTS ===
    @Slot(str)
    def update_label(self, msg: str):
        self.progress_dialog.ui.infoLabel.setText(msg)
    
    @Slot(int, int)
    def update_progress_bar(self, max_val: int, val: int):
        self.progress_dialog.ui.progressBar.setMaximum(max_val)
        self.progress_dialog.ui.progressBar.setValue(val)
        
    @Slot()
    def diplay_success_msg(self):
        self.progress_dialog.close()
        self.worker = None # clear the reference
        MessageHandler.show_info(self, 'Salesforce Export', 'Loading pricebook file to Salesforce has ended successfully!')
        
    @Slot(str)
    def display_failure_msg(self, msg: str):
        self.progress_dialog.close()
        self.worker = None
        MessageHandler.show_error(self, 'Salesforce Export', f"Error:\n'{msg}'")
        
    @Slot(str)
    def display_warning_msg(self, msg: str):
        self.progress_dialog.close()
        self.worker = None
        MessageHandler.show_error(self, 'Salesforce Export', msg)
    # ===========================
        
    
    
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    # from PySide6.QtCore import QTimer

    app = QApplication(sys.argv)

    main_menu = MainMenuWindow()
    main_menu.show()
    
    sys.exit(app.exec())
    