from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QApplication, QListWidgetItem, QSizePolicy, QMessageBox)

import pandas as pd

# for module testing
from pathlib import Path
from utils.xlsx_manager import get_sheets_from_file

from ui.ui_sheet_frame import Ui_SheetFrame

from views.widgets.currency_tab import CurrencyTab
from views.widgets.product2_row import Product2Row
from views.widgets.table_tab import TableTab

from dtos.session import AppSession

from core.mapper.mapper_model import SheetRule, PricebookConfig, ProductFieldMapping

# TODO: 
# - add sorting to pb list
# - walidacja sf_fields przy edycji za pomocą self.session (aktualne) i sf_target_field (sheet_rule)
# - walidacja sf_fields przy edycji za pomocą self.session (aktualne) i sf_target_field (sheet_rule)
class SheetTab(QWidget):
    
    def __init__(self, df: pd.DataFrame | None, sheet_name: str, sheet_rule: SheetRule | None, session: AppSession, parent=None):
        super().__init__()
        
        self.session = session
        self.df = df # sheet
        self.ui = Ui_SheetFrame()
        self.ui.setupUi(self)
        self.sheet_name = sheet_name
        self.sheet_rule = sheet_rule
        
        # currencies
        self.selected_pricebooks: set[str] = set() # holds active pricebook ids
        self.currency_tab_next_id = 0
        self.all_currency_tabs = {}
        
        # product2 fields
        self.next_prod2_row_id = 2 # 0: headers, 1: split line
        self.product2_rows: dict[str, Product2Row] = {}
        
        # preview tables
        self.tables: dict[str, QWidget] = {}
        
        # for testing __main__
        if self.session is None:
            self.make_session()
        
        self.setup_empty_frame()
        

    def make_session(self):
        from dtos.session import AppSession
        file_path = Path("./data/ab.xlsx")
        sheets = get_sheets_from_file(file_path)
        self.df = sheets["renewals"]
        self.session = AppSession()
        self.session.test_login()
        

    def _connect_signals(self):
        self.ui.pb_searchbar_line_edit.textChanged.connect(self.setup_pricebook_search)
        self.ui.pricebooks_list.itemChanged.connect(self.update_currency_tabs)
        self.ui.pricebooks_list.itemClicked.connect(self.activate_currency_tab)
        

    def load_pricebooks(self):
        ids_to_check = set()
        missing_ids = []

        if self.sheet_rule:
            available_sf_ids = self.session.sf_metadata.pricebooks.keys()
            valid_configs = []

            for config in self.sheet_rule.pricebook_configs:
                if config.pricebook_id in available_sf_ids:
                    valid_configs.append(config)
                    ids_to_check.add(config.pricebook_id)
                else:
                    missing_ids.append(config.pricebook_id)
            
            self.sheet_rule.pricebook_configs = valid_configs

        for i, (pb_id, pb_name) in enumerate(self.session.sf_metadata.pricebooks.items()):
            item = QListWidgetItem(pb_name)
            item.setData(Qt.UserRole, pb_id)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            
            if pb_id in ids_to_check:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

            self.ui.pricebooks_list.addItem(item)
            if i == 0:
                self.ui.pricebooks_list.setCurrentItem(item)

        if missing_ids:
            msg_text = (
                'Mapper file contains pricebooks that no longer exist in Salesforce\n'
                'Pricebooks that have been skipped:\n' + 
                '\n'.join(f'- ID: {pid}' for pid in missing_ids)
            )
            QMessageBox.warning(self, 'Invalid Mapper Data', msg_text)


    def activate_currency_tab(self, item: QListWidgetItem):
        pricebook_name = item.text()

        for i in range(self.ui.currency_tabs.count()):
            if self.ui.currency_tabs.tabText(i) == pricebook_name:
                self.ui.currency_tabs.setCurrentIndex(i)
                return
            

    def setup_pricebook_search(self, text):
        for i in range(self.ui.pricebooks_list.count()):
            item = self.ui.pricebooks_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())
            
            
    def load_product2_fields(self):
        
        def add_row_to_grid(grid, row, index):
            grid.addWidget(row.include_checkbox,     index, 0)
            grid.addWidget(row.name_label,           index, 1)
            grid.addWidget(row.field_combo,          index, 2)
            grid.addWidget(row.function_combo,       index, 3)
            grid.addWidget(row.allow_nulls_checkbox, index, 4)
        
        grid = self.ui.gridLayout_2
        grid.setColumnStretch(0, 0); grid.setColumnStretch(1, 2)
        grid.setColumnStretch(2, 3); grid.setColumnStretch(3, 3); grid.setColumnStretch(4, 1)

        valid_sf_prod2_fields: dict[str, dict] = self.session.sf_metadata.product2_fields
        df_columns = list(self.df.columns) if self.df is not None else []
        columns = df_columns
        
        existing_mappings = {} 

        if self.sheet_rule:
            # merging fields from df and snapshot
            columns = list(dict.fromkeys(df_columns + self.sheet_rule.source_schema_snapshot))
            
            for m in self.sheet_rule.product2_mappings:
                existing_mappings[m.sf_target_field] = m

        missing_keys = [k for k in existing_mappings.keys() if k not in valid_sf_prod2_fields]

        for field_name in missing_keys:
            mapping_config = existing_mappings[field_name]
            
            row = Product2Row(
                field_name=field_name,
                field_metadata=None,
                sheet_columns=columns,
                field_mapping=mapping_config,
                parent=self.ui.product_fields_scroll_area_contents
            )
            self.product2_rows[field_name] = row
            add_row_to_grid(grid, row, self.next_prod2_row_id)
            self.next_prod2_row_id += 1
            
        for field_name, field_metadata in valid_sf_prod2_fields.items():            
            mapping_config = existing_mappings.get(field_name)

            row = Product2Row(
                field_name=field_name,
                field_metadata=field_metadata,
                sheet_columns=columns,
                field_mapping=mapping_config, # can be None -> means its new mapper or not configerd field
                parent=self.ui.product_fields_scroll_area_contents
            )

            self.product2_rows[field_name] = row
            add_row_to_grid(grid, row, self.next_prod2_row_id)   
            self.next_prod2_row_id += 1

    
    # ==== SETTING UP NEW SHEET TAB =====
    def setup_empty_frame(self):
        self._connect_signals()
        self.load_pricebooks()
        self.create_currency_tabs()
        self.update_currency_tabs()
        self.load_product2_fields()
        self.create_table_tabs()
        
            
   # ---- CURRENCY TABS MANAGEMENT
    def create_currency_tabs(self):
        pb_configs_map = {}
        invalid_currency_codes = set()
        valid_available_currencies = self.session.sf_metadata.available_currencies

        if self.sheet_rule:
            for pb_config in self.sheet_rule.pricebook_configs:
                valid_currencies_for_config = []
                
                for currency_config in pb_config.currencies:
                    code = currency_config.code
                    
                    if code not in valid_available_currencies:
                        invalid_currency_codes.add(code)
                    else:
                        valid_currencies_for_config.append(currency_config)
                
                pb_config.currencies = valid_currencies_for_config
                pb_configs_map[pb_config.pricebook_id] = pb_config

            if invalid_currency_codes:
                msg_text = (
                    'Mapper file contains currencies that are no longer available in your Salesforce configuration:\n' +
                    '\n'.join(f'- {code}' for code in sorted(invalid_currency_codes))
                )
                QMessageBox.warning(self, 'Invalid Mapper Data', msg_text)

        available_cols = list(self.df.columns) if self.df is not None else []
        
        if self.sheet_rule:
            available_cols = list(dict.fromkeys(self.sheet_rule.source_schema_snapshot + available_cols))

        for pb_id, pb_name in self.session.sf_metadata.pricebooks.items():
            idx = self.currency_tab_next_id
            self.currency_tab_next_id += 1
            
            specific_config = pb_configs_map.get(pb_id)

            tab = CurrencyTab(
                tab_id=idx, 
                available_currencies=valid_available_currencies, 
                columns=available_cols,
                pricebook_config=specific_config
            )     
            self.all_currency_tabs[f'{pb_id}'] = tab
            
    
    def update_currency_tabs(self):
        self.ui.currency_tabs.clear()
        self.selected_pricebooks.clear()
        
        for i in range(self.ui.pricebooks_list.count()):
            item = self.ui.pricebooks_list.item(i)
            if item.checkState() == Qt.Checked:
                pb_id = item.data(Qt.UserRole)
                pb_name = item.text()   
                tab_to_load = self.all_currency_tabs[pb_id]
                self.ui.currency_tabs.addTab(tab_to_load, pb_name)
                self.selected_pricebooks.add(pb_id)


    # ---- TABLE TABS MANAGEMENT
    def create_table_tabs(self):
        # product2-preview, 'filename'.xlsx
        if self.df is not None:
            file_preview_table = TableTab(self.sheet_name, self.df)
            product2_table = TableTab('Product2 Preview', self.df)
            
            self.ui.xlsx_tabs.addTab(file_preview_table, self.sheet_name)
            self.ui.xlsx_tabs.addTab(product2_table, 'Product2 Preview')
       
    
    # ---- DTOS
    def get_sheet_config(self) -> SheetRule:
        
        columns = self.df.columns.tolist() if self.df is not None else self.sheet_rule.source_schema_snapshot
        
        return SheetRule(
            sheet_name=self.sheet_name,
            source_schema_snapshot=columns,
            pricebook_configs=self.get_pricebook_configs(),
            product2_mappings=self.get_product2_mappings()
        )
        
        
    def get_pricebook_configs(self) -> list[PricebookConfig]:
        data = [] # pricebook_configs
        
        for pb_id in self.selected_pricebooks:
            tab = self.all_currency_tabs[pb_id]
            pricebook_config = tab.get_pricebook_config(pb_id)
            data.append(pricebook_config)
        return data
    

    def get_product2_mappings(self) -> list[ProductFieldMapping]:
        data = [] # product2_mappings
        
        for row_widget in self.product2_rows.values():
            field_mapping = row_widget.get_product2_mapping()
            data.append(field_mapping)
        return data
            

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = SheetTab(None, None, None)
    window.show()

    sys.exit(app.exec())