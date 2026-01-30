from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QApplication, QListWidgetItem, QSizePolicy)

import pandas as pd

# for module testing
from pathlib import Path
from utils.xlsx_manager import get_sheets_from_file

from ui.ui_sheet_frame import Ui_SheetFrame

from views.widgets.currency_tab import CurrencyTab
from views.widgets.product2_row import Product2Row
from views.widgets.table_tab import TableTab

from core.mapper.mapper_model import SheetRule, PricebookConfig, ProductFieldMapping

# TODO: 
# - add sorting to pb list
# - add indexes to column names in combos
class SheetTab(QWidget):
    
    def __init__(self, df: pd.DataFrame | None, sheet_name: str, editor, parent=None):
        super().__init__()
        self.editor = editor
        self.ui = Ui_SheetFrame()
        self.ui.setupUi(self)
        self.sheet_name = sheet_name
        
        # currencies
        self.selected_pricebooks: set[str] = set() # holds active pricebook ids
        self.currency_tab_next_id = 0
        self.all_currency_tabs = {}
        
        # product2 fields
        self.next_prod2_row_id = 2 # 0: headers, 1: split line
        self.product2_rows: dict[str, Product2Row] = {}
        
        # preview tables
        self.tables: dir[str, QWidget] = {}
        
        if self.editor is None:
            # tryb testowy – widget uruchamiany samodzielnie
            self.assign_editor_for_testing()
        else:
            self.df = df # sheet
        
        self.setup_empty_frame()
        

    def assign_editor_for_testing(self):
        from views.mapper_editor_window import MapperEditorWindow
        from dtos.session import AppSession
        file_path = Path("./data/ab.xlsx")
        sheets = get_sheets_from_file(file_path)
        self.df = sheets["renewals"]
        session = AppSession()
        session.test_login()
        self.editor = MapperEditorWindow(session, None)
        

    def _connect_signals(self):
        self.ui.pb_searchbar_line_edit.textChanged.connect(self.setup_pricebook_search)
        self.ui.pricebooks_list.itemChanged.connect(self.update_currency_tabs)
        self.ui.pricebooks_list.itemClicked.connect(self.activate_currency_tab)
        

    def load_pricebooks(self):
        # for i, pb in enumerate(self.editor.user_sf_data['pricebooks']):
        for i, (pb_id, pb_name) in enumerate(self.editor.session.sf_metadata.pricebooks.items()):
            item = QListWidgetItem(pb_name)

            item.setData(Qt.UserRole, pb_id)

            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)

            self.ui.pricebooks_list.addItem(item)

            if i == 0:
                self.ui.pricebooks_list.setCurrentItem(item)


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
        grid = self.ui.gridLayout_2
        grid.setColumnStretch(0, 0)   # checkbox
        grid.setColumnStretch(1, 2)   # label
        grid.setColumnStretch(2, 3)   # source
        grid.setColumnStretch(3, 3)   # function
        grid.setColumnStretch(4, 1)   # allow empty

        for field_name, field_data in self.editor.session.sf_metadata.product2_fields.items():
            row = Product2Row(
                field_name=field_name,
                field_metadata=field_data,
                sheet_columns=list(self.df.columns),
                parent=self.ui.product_fields_scroll_area_contents
            )

            self.product2_rows[field_name] = row
            row_index = self.next_prod2_row_id

            grid.addWidget(row.include_checkbox,     row_index, 0)
            grid.addWidget(row.name_label,           row_index, 1)
            grid.addWidget(row.field_combo,          row_index, 2)
            grid.addWidget(row.function_combo,       row_index, 3)
            grid.addWidget(row.allow_nulls_checkbox, row_index, 4)

            self.next_prod2_row_id += 1
    # OLD 
    # def load_product2_fields(self):
    #     for field_name, field_data in self.editor.session.sf_metadata.product2_fields.items():
    #         row_widget = Product2Row(
    #             field_name=field_name, 
    #             field_metadata=field_data,
    #             sheet_columns=list(self.df.columns), 
    #             parent=self.ui.product_fields_scroll_area_contents
    #         )
    #         self.product2_rows[field_name] = row_widget
    #         self.ui.gridLayout_2.addWidget(row_widget, self.next_prod2_row_id, 0, 1, 4)
    #         self.next_prod2_row_id += 1
            
    
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
        for pb_id, pb_name in self.editor.session.sf_metadata.pricebooks.items():
            idx = self.currency_tab_next_id
            self.currency_tab_next_id += 1
    
            tab = CurrencyTab(idx, self.editor.session.sf_metadata.available_currencies, list(self.df.columns))
            
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
        file_preview_table = TableTab(self.sheet_name, self.df)
        product2_table = TableTab('Product2 Preview', self.df)
        
        self.ui.xlsx_tabs.addTab(file_preview_table, self.sheet_name)
        self.ui.xlsx_tabs.addTab(product2_table, 'Product2 Preview')
       
    
    # ---- DTOS
    def get_sheet_config(self) -> SheetRule:
        
        return SheetRule(
            sheet_name=self.sheet_name,
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