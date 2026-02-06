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
from views.widgets.dialog_boxes.column_mapping_dialog import ColumnMappingDialog

from core.mapper.mapper_model import MapperModel, SheetRule
from dtos.session import AppSession
from exceptions.gui_exceptions import MappingNotSetError


class MapperEditorWindow(QWidget):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    
    def __init__(self, session: AppSession, mapper_path=None):
        super().__init__()
        session.validate()
        self.session = session
        
        self.ui = Ui_MapperEditor()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon())
        
        # GLOBAL VALUES
        self.path_to_pricebook = None
        self.sheet_tabs = {} # QWidgets representing each sheet's config
        self.mapper_config = None
    
        # LOADED SHEETS
        self.all_sheets = {} # all dataframes from file
        self.sheets = {} # selected dataframes by user

        self._connect_signals()
        
        # ==== EDITING EXISTING MAPPER LOGIC ====
        if mapper_path:
            self.mapper_config = self.load_mapper_file(mapper_path)
            self.ui.mapper_name_line_edit.setText(self.mapper_config.name)
            self.add_sheet_tabs()
            self.ui.save_mapper_button.setEnabled(True)
        
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
            # self.mapper_config = None
            self.load_xlsx_file() # load data from chosen file
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

    
    # overriding mapper info after new .xlsx file is provided (in mapper editing mode)
    def migrate_rule_to_new_columns(self, sheet_rule: SheetRule, column_map: dict, new_columns_list: list[str]):
        for mapping in sheet_rule.product2_mappings:
            # raw source_column
            if mapping.source_column and mapping.source_column in column_map:
                mapping.source_column = column_map[mapping.source_column]
            
            # mapping args
            if mapping.args:
                if 'source_column' in mapping.args:
                    old_col = mapping.args['source_column']
                    if old_col in column_map:
                        mapping.args['source_column'] = column_map[old_col]
                        
                if 'source_columns' in mapping.args:
                    current_list = mapping.args['source_columns']
                    if isinstance(current_list, list):
                        new_list = []
                        for col in current_list:
                            new_list.append(column_map.get(col, col))
                        mapping.args['source_columns'] = new_list
                # place for future function's args management

        for pb_config in sheet_rule.pricebook_configs:
            for curr_mapping in pb_config.currencies:
                if curr_mapping.source_column in column_map:
                    curr_mapping.source_column = column_map[curr_mapping.source_column]
                    
        sheet_rule.source_schema_snapshot = new_columns_list


    # OLD LOGIC add_sheet_tabs
    # def add_sheet_tabs(self):
    #     if self.mapper_config is None: # from file (new mapper)
    #         for name, sheet in self.sheets.items():
    #             new_tab = SheetTab(sheet, name, None, self.session, self)
    #             self.sheet_tabs[name] = new_tab
    #             self.ui.sheet_tabs.addTab(new_tab, name)
    #     else: # from mapper config (editing existing mapper)
    #         for sheet_rule in self.mapper_config.sheet_rules:
    #             new_tab = SheetTab(None, sheet_rule.sheet_name, sheet_rule, self.session, self)
    #             self.sheet_tabs[sheet_rule.sheet_name] = new_tab
    #             self.ui.sheet_tabs.addTab(new_tab, sheet_rule.sheet_name)
    
    def add_sheet_tabs(self):
        if self.sheets: # excel file loaded
            existing_rules_map = {}
            if self.mapper_config: # if mapper in editing mode and excel file loaded
                for rule in self.mapper_config.sheet_rules:
                    existing_rules_map[rule.sheet_name] = rule

            for name, sheet_df in self.sheets.items():
                rule_for_sheet = existing_rules_map.get(name)
                
                if rule_for_sheet:
                    missing_cols = [ # mapper cols missing in excel file
                        col for col in rule_for_sheet.source_schema_snapshot 
                        if col not in sheet_df.columns
                    ]
                    
                    if missing_cols:
                        dialog = ColumnMappingDialog(
                            rule_for_sheet.source_schema_snapshot, 
                            sheet_df.columns.tolist(), 
                            name, 
                            self
                        )
                        
                        if dialog.exec():
                            excel_to_mapper_map = dialog.get_mapping() 
                            
                            # get_mapping returns {Excel: Mapper}, we need {Mapper: Excel}
                            mapper_to_excel_map = {v: k for k, v in excel_to_mapper_map.items()}
                            
                            self.migrate_rule_to_new_columns(
                                rule_for_sheet, 
                                mapper_to_excel_map, 
                                sheet_df.columns.tolist()
                            )
                        else:
                            pass
                        
                new_tab = SheetTab(sheet_df, name, rule_for_sheet, self.session, self)
                self.sheet_tabs[name] = new_tab
                self.ui.sheet_tabs.addTab(new_tab, name)
                
        elif self.mapper_config: # mapper in edit mode without excel file provided
            for sheet_rule in self.mapper_config.sheet_rules:
                name = sheet_rule.sheet_name
                new_tab = SheetTab(None, name, sheet_rule, self.session, self)
                self.sheet_tabs[name] = new_tab
                self.ui.sheet_tabs.addTab(new_tab, name)
    
    
    # ==== EDITING EXISTING MAPPER =====
    def load_mapper_file(self, mapper_path):
        try:
            with open(mapper_path, 'r', encoding='utf-8') as mapper_file:
                mapper_dict = json.load(mapper_file)
                return MapperModel.from_dict(mapper_dict)
        except FileNotFoundError:
            raise FileNotFoundError(f"Mapper file does not exist: '{mapper_path}'.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: '{mapper_path}'.")
                
    
    # ==== SAVING MAPPER ======
    def save_mapper(self):
        # TODO: add mapper name to user data
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
    from dtos.session import AppSession
    from core.profile.profile_model import Profile
    from views.mapper_editor_window import MapperEditorWindow
    from salesforce_api.salesforce_api import SalesforceApi

    profile = Profile.from_json('./cert/test_creds.json')    
    sf_api = SalesforceApi(profile)
    sf_api.connect()

    session = AppSession()
    session.login(
        user_id='123213', 
        sf_metadata=sf_api.get_user_sf_metadata()
    )
    # session.test_login()

    app = QApplication(sys.argv)

    # window = MapperEditorWindow(session, None)
    window = MapperEditorWindow(session, './mappers/invalid-ab-mapper.json')
    window.show()

    sys.exit(app.exec())