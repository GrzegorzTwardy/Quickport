from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QMessageBox)
from PySide6.QtGui import QIcon

import os
import json
from pathlib import Path

from ui.ui_mapper_editor import Ui_MapperEditor
from utils.xlsx_manager import get_sheets_from_file

from views.widgets.sheet_tab import SheetTab
from views.widgets.dialog_boxes.checklist_dialog import execute_checklist_dialog
from views.widgets.dialog_boxes.overwrite_dialog import overwrite_dialog_result
from views.widgets.dialog_boxes.confirm_warning_dialog import confirm_warning_result

from core.mapper.mapper_model import MapperModel, SheetRule
from dtos.session import AppSession
from exceptions.gui_exceptions import MappingNotSetError


class MapperEditorWindow(QWidget):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    
    def __init__(self, session: AppSession, mapper_config=None):
        super().__init__()
        session.validate()
        self.session = session
        
        self.ui = Ui_MapperEditor()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon())
        
        # GLOBAL VALUES
        self.path_to_pricebook = None
        self.sheet_tabs = {} # QWidgets representing each sheet's config
    
        # LOADED SHEETS
        self.all_sheets = {} # all dataframes from file
        self.sheets = {} # selected dataframes by user

        # ==== SETTING UP MAPPER ====
        self.setup_empty_mapper()
        
        # ==== LOADING CONFIG (if editing existing mapper) ====
        if mapper_config:
            self.load_mapper_config()
        
        self.ui.mapper_name_line_edit.setFocus()
        

    def _connect_signals(self):
        self.ui.choose_file_button.clicked.connect(self.open_file_dialog)
        self.ui.save_mapper_button.clicked.connect(self.save_mapper)
        self.ui.cancel_editing_button.clicked.connect(self.close_mapper)
    
    
    def close_mapper(self):
        msg = 'Do you want to close the editor without saving?'
        if confirm_warning_result('Closing Mapper Editor', msg):
            self.close()
    
    
    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Choose pricebook file", 
            "", 
            "Excel files (*.xlsx *.xls)"
        )
        if file_path:
            self.ui.input_file_label.setText(f'"{os.path.basename(file_path)}"')
            self.path_to_pricebook = file_path
            # load data from chosen file
            self.load_xlsx_file()
            self.ui.save_mapper_button.setEnabled(True)
            
            
    # for testing purposes
    def auto_select_xlsx_TEST(self):
        self.path_to_pricebook = Path('./data/ab.xlsx')
        self.ui.input_file_label.setText(f'"{self.path_to_pricebook}"')
        
        self.all_sheets = get_sheets_from_file(self.path_to_pricebook)
        self.sheets['renewals'] = self.all_sheets['renewals']
        # self.sheets['Active OM SKUs'] = self.all_sheets['Active OM SKUs']
        self.add_sheet_tabs()
        
        
    def clear_sheet_tabs(self):
        self.sheets.clear()
        self.sheet_tabs.clear()
        while self.ui.sheet_tabs.count() > 0:
            widget = self.ui.sheet_tabs.widget(0)
            self.ui.sheet_tabs.removeTab(0)
            widget.deleteLater()    

    
    # replacing sheets when new file was chosen
    def confirm_replace_sheets(self) -> bool:
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Replace sheets")
        msg.setText("Current configuration will not be saved.")
        msg.setInformativeText("Do you want to continue?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)

        return msg.exec() == QMessageBox.Ok
    
    
    def load_xlsx_file(self):
        self.all_sheets = get_sheets_from_file(self.path_to_pricebook)
        
        # user selects sheets to add
        sheet_names = [name for name in self.all_sheets.keys()]
        selected_sheets = execute_checklist_dialog(sheet_names, user_operation='Choose sheets to add', parent=None)
        
        # canceled
        if not selected_sheets:
            return
        
        # confirmation for overriding existing sheets (if they exist)
        if self.sheets:
            if not self.confirm_replace_sheets():
                return
        
        self.clear_sheet_tabs()
    
        if selected_sheets:
            for name in selected_sheets:
                self.sheets[name] = self.all_sheets[name]
        
        self.add_sheet_tabs()

    
    def add_sheet_tabs(self):
        for name, sheet in self.sheets.items():
            new_tab = SheetTab(sheet, name, self)
            self.sheet_tabs[name] = new_tab
            self.ui.sheet_tabs.addTab(new_tab, name)
    
    
    # ==== SETTING UP EMPTY MAPPER =====
    def setup_empty_mapper(self):
        self._connect_signals()
        # TODO: sf_api.connect_to_salesforce()
        
        # ==== TESTING =====
        self.auto_select_xlsx_TEST()
        # ==================
        
    
    # ==== EDITING EXISTING MAPPER =====
    def load_mapper_config(self):
        pass
    
    
    # ==== SAVING MAPPER ======
    def save_mapper(self):
        try:
            # collecting data
            mapper_name = self.ui.mapper_name_line_edit.text()
            mapper_name = mapper_name
            owner_id = self.session.user_id
            
            sheet_rules: list[SheetRule] = []
            
            for sheet_tab in self.sheet_tabs.values():
                # individual sheet settings
                new_rule = sheet_tab.get_sheet_config()
                sheet_rules.append(new_rule)
            
            # creating to mapper
            mapper = MapperModel(
                name=mapper_name,
                owner_id=owner_id,
                sheet_rules=sheet_rules
            )
            
            # saving mapper
            path_to_file = Path(self.PATH_TO_MAPPERS) / f"{mapper.name}.json"
            should_save = True

            if path_to_file.exists():
                should_save = overwrite_dialog_result(f'{mapper.name}.json')

            if should_save:
                with open(path_to_file, 'w', encoding='utf-8') as f:
                    json.dump(mapper.to_dict(), f, indent=4)
                    
                QMessageBox.information(
                    self,
                    'Mapper Saved',
                    f'Mapper "{mapper.name}" has been saved.'
                )
                self.close()

        except MappingNotSetError as e:
            QMessageBox.warning(self, 'Mapping Error', str(e))

            

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    session = AppSession()
    session.test_login()

    app = QApplication(sys.argv)

    window = MapperEditorWindow(session, None)
    window.show()

    sys.exit(app.exec())
