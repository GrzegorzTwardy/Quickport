from PySide6.QtWidgets import QWidget, QListWidgetItem, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

import json
from pathlib import Path

from views.mapper_editor_window import MapperEditorWindow
from ui.ui_mapper_list import Ui_MapperListMain
from dtos.session import AppSession


# TODO: aktualizacja listy po zamknięciu okna MapperEditorWindow
class MapperListWindow(QWidget):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    
    def __init__(self, session: AppSession):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.session = session
        
        self.ui = Ui_MapperListMain()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon())
        
        # === views ===
        self.editor_new = None
        self.editor_editing = None
        # =============
        
        # self.available_mappers = {} # name: path
        self.current_mapper_path = ''
        self.selected_mapper_idx = 0
        
        self._connect_signals()
        self.loadMappers()
        
    
    def _connect_signals(self):
        self.ui.mapperList.currentRowChanged.connect(self.on_item_selected)
        self.ui.addButton.clicked.connect(self.add_new_mapper)
        self.ui.editButton.clicked.connect(self.edit_mapper)
        self.ui.deleteButton.clicked.connect(self.delete_mapper)
    
    
    def on_item_selected(self, row: int):
        self.selected_mapper_idx = row
        item = self.ui.mapperList.item(row)
        if item is not None:
            self.current_mapper_path = item.data(Qt.UserRole)
            
        
    def loadMappers(self):
        self.ui.mapperList.clear()
        
        for json_file in self.PATH_TO_MAPPERS.glob('*.json'):
            mapper_name = json_file.stem
            mapper_item = QListWidgetItem(mapper_name)
            mapper_item.setData(Qt.UserRole, json_file)
            self.ui.mapperList.addItem(mapper_item)
            # self.available_mappers[mapper_name] = mapper_item
        if self.ui.mapperList.count() > 0:
            try:
                self.ui.mapperList.setCurrentRow(self.selected_mapper_idx)
            except IndexError:
                self.ui.mapperList.setCurrentRow(0)
            self.ui.editButton.setEnabled(True)
            self.ui.deleteButton.setEnabled(True)
    
    
    def add_new_mapper(self):
        if self.editor_new is None:
            self.editor_new = MapperEditorWindow(self.session, None)
            self.editor_new.refresh_mapper_list.connect(self.loadMappers)
            self.editor_new.destroyed.connect(lambda: setattr(self, 'editor_new', None))
            self.editor_new.show()
        else:
            self.editor_new.show()
            self.editor_new.activateWindow()
        
        if not self.ui.editButton.isEnabled():
            self.ui.editButton.setEnabled(True)
        if not self.ui.deleteButton.isEnabled():
            self.ui.deleteButton.setEnabled(True)
            
            
    def edit_mapper(self):
        if self.editor_editing is not None: # if window is already opened but user selected another mapper to edit
            self.editor_editing.close() # close old edit window
            
        if self.editor_editing is None:
            self.editor_editing = MapperEditorWindow(self.session, self.current_mapper_path)
            self.editor_editing.refresh_mapper_list.connect(self.loadMappers)
            self.editor_editing.destroyed.connect(lambda: setattr(self, 'editor_editing', None))
            self.editor_editing.show()
        else:
            self.editor_editing.show()
            self.editor_editing.activateWindow()
            
    
    def delete_mapper(self):
        result = QMessageBox.question(
            self,
            'Deleting Mapper',
            f"Are you sure you want to delete '{self.current_mapper_path.stem}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if result:
            self.current_mapper_path.unlink()
            self.ui.mapperList.takeItem(self.selected_mapper_idx)
            
            if self.ui.mapperList.count() > 0:
                self.ui.mapperList.setCurrentRow(0)
                self.on_item_selected(0)
            else:
                self.current_mapper_path = None
                self.selected_mapper_idx = -1
                self.ui.editButton.setEnabled(False)
                self.ui.deleteButton.setEnabled(False)
                
            self.loadMappers()
                
        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    from dtos.session import AppSession
    from core.profile.profile_model import Profile
    from salesforce_api.salesforce_api import SalesforceApi

    profile = Profile.from_json('./cert/test_creds.json')    
    sf_api = SalesforceApi(profile)
    sf_api.connect()
    
    app = QApplication(sys.argv)
    
    session = AppSession()
    session.test_login()
    # session.login(
    #     user_id='123213', 
    #     sf_metadata=sf_api.get_user_sf_metadata()
    # )

    window = MapperListWindow(session)
    window.show()

    sys.exit(app.exec())