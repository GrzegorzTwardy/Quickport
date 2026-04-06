import json
from pathlib import Path
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QFileDialog)
from PySide6.QtCore import Qt, Slot

from core.settings.settings_manager import settings_manager
from exceptions.global_exceptions import *
from ui.ui_main_menu import Ui_MainMenu

from views.mapper_list_window import MapperListWindow
from views.profile_manager_window import ProfileManagerWindow
from views.widgets.progress_bar_dialog import ProgressBarDialog
from views.widgets.dialog_boxes.settings_dialog import SettingsDialog
from views.widgets.dialog_boxes.about_dialog import AboutDialog
from utils.message_handler import MessageHandler
from thread_workers.sf_export_worker import SalesforceExportWorker
from thread_workers.csv_export_worker import CsvExportWorker


class MainMenuWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        
        self.session = AppSession()
        self.full_name = None
        self.env_name = None
        self.sf_api = None
        # self.primary_key = None
        
        # views
        self.profile_manager_window = None
        self.mapper_list_window = None
        
        # mapping config
        self.pricebook_path = None
        
        self._connect_signals()
        
    @property
    def path_to_mappers(self):
        return settings_manager.get_setting('mappers_path')
    
    def test_login(self):
        pass
    
    def _connect_signals(self):
        self.session.user_logged_in.connect(self.on_login)
        self.session.user_logged_out.connect(self.on_logout)
        self.ui.mappersButton.clicked.connect(self.open_mapper_list)
        self.ui.chooseFileButton.clicked.connect(self.open_file_dialog)
        self.ui.loadToSfButton.clicked.connect(self.load_data_to_Sf)
        self.ui.profilesButton.clicked.connect(self.open_profile_manager)
        self.ui.exportCsvButton.clicked.connect(self.export_data_to_csv)
        self.ui.actionSettings.triggered.connect(self.open_settings_dialog)
        self.ui.actionShowInfo.triggered.connect(self.open_about_dialog)
    
    
    def open_settings_dialog(self):
        dialog = SettingsDialog(self)
        dialog.show()
        
        
    def open_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.show()
    
    
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
            self.env_name = self.profile_manager_window.env_name
            self.sf_api = self.profile_manager_window.sf_api
            self.session.primary_key = self.profile_manager_window.primary_key
            # self.primary_key = self.profile_manager_window.primary_key

        self.ui.exportPricebookGroupBox.setEnabled(True)
        self.ui.mappersButton.setEnabled(True)
        
        display_name = self.full_name if self.full_name else '-none-'
        display_env = self.env_name if self.env_name else '-none-'
        self.ui.currentUsernameLabel.setText(display_name)
        self.ui.currentSfEnvLabel.setText(display_env)
        
        self.load_mappers()
    
    
    def on_logout(self):
        self.ui.exportPricebookGroupBox.setEnabled(False)
        self.ui.mappersButton.setEnabled(False)
        self.ui.currentUsernameLabel.setText('-none-')        
            
        
    def open_mapper_list(self):
        if self.mapper_list_window is None:
            self.mapper_list_window = MapperListWindow(self.session, self)
            self.mapper_list_window.list_changed.connect(self.load_mappers)
            self.mapper_list_window.destroyed.connect(lambda: setattr(self, 'mapper_list_window', None))
            self.mapper_list_window.show()
        else:
            self.mapper_list_window.show()
            self.mapper_list_window.activateWindow()
            
    
    def load_mappers(self):
        self.ui.mapperList.clear()
        
        for json_file in Path(self.path_to_mappers).glob('*.json'):
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
    
    
    def set_export_buttons_enabled(self, state: bool):
        self.ui.loadToSfButton.setEnabled(state)
        self.ui.exportCsvButton.setEnabled(state)
    
    
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
        
        self.set_export_buttons_enabled(False)
        
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
        
        self.worker.finished_success.connect(lambda: self.diplay_success_msg('Salesforce Export'))
        self.worker.finished_error.connect(lambda msg: self.display_failure_msg('Salesforce Export', msg))
        self.worker.finished_warning.connect(lambda msg: self.display_warning_msg('Salesforce Export', msg))
        
        self.worker.finished.connect(self.worker.deleteLater)
        
        self.worker.start()
        
    
    def export_data_to_csv(self):
        current_item = self.ui.mapperList.currentItem()
        if not current_item:
            MessageHandler.show_warning(self, 'Selection Error', 'Please select a mapper first.')
            return
            
        mapper_path = current_item.data(Qt.UserRole)
        
        self.set_export_buttons_enabled(False)
        
        self.progress_dialog = ProgressBarDialog('Setting up CSV export...')
        self.progress_dialog.show()
        
        self.worker = CsvExportWorker(
            mapper_path=mapper_path,
            pricebook_path=self.pricebook_path,
            session=self.session
        )
        
        self.worker.update_label.connect(self.update_label)
        self.worker.update_progress_bar.connect(self.update_progress_bar)
        
        self.worker.finished_success.connect(lambda: self.diplay_success_msg('CSV Export'))
        self.worker.finished_error.connect(lambda msg: self.display_failure_msg('CSV Export', msg))
        self.worker.finished_warning.connect(lambda msg: self.display_warning_msg('CSV Export', msg))
        
        self.worker.finished.connect(self.worker.deleteLater)
        
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
    def diplay_success_msg(self, title: str):
        self.progress_dialog.close()
        self.set_export_buttons_enabled(True)
        MessageHandler.show_info(self, title, 'Operation completed successfully!')
        
    @Slot(str)
    def display_failure_msg(self, title: str, msg: str):
        self.progress_dialog.close()
        self.set_export_buttons_enabled(True)
        MessageHandler.show_error(self, title, f"Error:\n'{msg}'")
        
    @Slot(str)
    def display_warning_msg(self, title: str, msg: str):
        self.progress_dialog.close()
        self.set_export_buttons_enabled(True)
        MessageHandler.show_error(self, title, msg)
    # ===========================
    
    
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    # from PySide6.QtCore import QTimer

    app = QApplication(sys.argv)

    main_menu = MainMenuWindow()
    main_menu.show()
    
    sys.exit(app.exec())
    