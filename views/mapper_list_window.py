from PySide6.QtWidgets import QWidget, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Signal

import json
from pathlib import Path

from core.settings.settings_manager import settings_manager
from views.mapper_editor_window import MapperEditorWindow
from ui.ui_mapper_list import Ui_MapperListMain
from dtos.session import AppSession


class MapperListWindow(QWidget):
    
    list_changed = Signal()
    
    def __init__(self, session: AppSession):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.session = session
        
        self.ui = Ui_MapperListMain()
        self.ui.setupUi(self)
        
        # === views ===
        self.editor_new = None
        self.opened_editors = {} # path: MapperEditorWindow instance
        # =============
        
        self.current_mapper_path = ''
        self.selected_mapper_idx = 0
        
        self._connect_signals()
        self.load_mappers()
        
    
    @property
    def path_to_mappers(self):
        return settings_manager.get_setting('mappers_path')
    
    
    def _connect_signals(self):
        self.ui.mapperList.currentRowChanged.connect(self.on_item_selected)
        self.ui.addButton.clicked.connect(self.add_new_mapper)
        self.ui.editButton.clicked.connect(self.edit_mapper)
        self.ui.deleteButton.clicked.connect(self.delete_mapper)
        self.ui.backButton.clicked.connect(lambda: self.close())
    
    
    def on_item_selected(self, row: int):
        self.selected_mapper_idx = row
        item = self.ui.mapperList.item(row)
        if item is not None:
            self.current_mapper_path = item.data(Qt.UserRole)
            
        
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
            try:
                self.ui.mapperList.setCurrentRow(self.selected_mapper_idx)
            except IndexError:
                self.ui.mapperList.setCurrentRow(0)
            self.ui.editButton.setEnabled(True)
            self.ui.deleteButton.setEnabled(True)
        
        self.list_changed.emit()
    
    
    def add_new_mapper(self): # singleton
        if self.editor_new is None:
            self.editor_new = MapperEditorWindow(self.session, None)
            self.editor_new.refresh_mapper_list.connect(self.load_mappers)
            self.editor_new.destroyed.connect(lambda: setattr(self, 'editor_new', None))
            self.editor_new.show()
        else:
            self.editor_new.show()
            self.editor_new.raise_()
            self.editor_new.activateWindow()
        
        if not self.ui.editButton.isEnabled():
            self.ui.editButton.setEnabled(True)
        if not self.ui.deleteButton.isEnabled():
            self.ui.deleteButton.setEnabled(True)
            
            
    def edit_mapper(self): 
        if not self.current_mapper_path:
            return

        target_path = self.current_mapper_path

        if target_path in self.opened_editors:
            existing_window = self.opened_editors[target_path]
            existing_window.show()
            existing_window.raise_()
            existing_window.activateWindow()
            return

        new_window = MapperEditorWindow(self.session, target_path)
        new_window.refresh_mapper_list.connect(self.load_mappers)
        
        self.opened_editors[target_path] = new_window
        
        new_window.destroyed.connect(lambda: self.cleanup_editor(target_path))
        new_window.show()
    
    
    def cleanup_editor(self, path): # remove window instance from dict
        if path in self.opened_editors:
            del self.opened_editors[path]        
    
    
    def delete_mapper(self):
        result = QMessageBox.question(
            self,
            'Deleting Mapper',
            f"Are you sure you want to delete '{self.current_mapper_path.stem}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if result == QMessageBox.Yes:
            if self.current_mapper_path in self.opened_editors:
                self.opened_editors[self.current_mapper_path].close()
            
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
                
            self.load_mappers()
                
        
if __name__ == "__main__":
    pass