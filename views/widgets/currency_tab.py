from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QGridLayout, QWidget, QScrollArea, QFrame, QPushButton, QMessageBox, QSizePolicy)

from views.widgets.currency_row import CurrencyRow
from views.widgets.dialog_boxes.checklist_dialog import execute_checklist_dialog

from core.mapper.mapper_model import PricebookConfig, CurrencyMapping


class CurrencyTab(QWidget):
    
    def __init__(self, index: int, available_currencies: list[str], sheet_columns: list[str]):
        super().__init__()
        self._available_currencies: set[str] = set(available_currencies)
        self.sheet_columns = sheet_columns
        self.next_row_id = 2 # 0: headers, 1: split line
        
        self.currency_rows: dict[str, CurrencyRow] = {}
        
        self.setup_ui(index)
        

    def update_remove_button_state(self):
        self.remove_btn.setEnabled(bool(self.currency_rows))


    def add_new_currencies(self):
        selected_currencies = execute_checklist_dialog(
            self._available_currencies, 
            user_operation='Choose currencies to add', 
            parent=self
        )
        
        if selected_currencies:
            for i, c in enumerate(selected_currencies):
                row_index = self.next_row_id
                self.next_row_id += 1
                
                row_widget = CurrencyRow(c, self.sheet_columns, self.frame, self.frame_layout)
                self.frame_layout.addWidget(row_widget, row_index, 0, 1, 4)
                
                if i == 0:
                    row_widget.c_factor_ledit.setFocus()

                # removing new currency from available ones
                self._available_currencies.remove(c)
                
                # adding row widget
                self.currency_rows[c] = row_widget
                
                if len(self._available_currencies) == 0:
                    self.add_btn.setEnabled(False)
                    
            self.update_remove_button_state()

    
    def remove_currencies(self):
        currency_rows_codes = [key for key in self.currency_rows.keys()]
        selected_codes: list[str] = execute_checklist_dialog(
            currency_rows_codes, 
            user_operation='Choose currencies to remove', 
            parent=self
        )
        
        if not selected_codes:
            return

        codes_str = ', '.join(selected_codes)

        reply = QMessageBox.question(
            self,
            'Removing currencies',
            f'Do you want to remove currencies:\n{codes_str}?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return
        
        for code in selected_codes:
            widget = self.currency_rows.pop(code)
            self.frame_layout.removeWidget(widget)
            self._available_currencies.add(code)
            widget.deleteLater()
        
        self.add_btn.setEnabled(bool(self._available_currencies))
        self.update_remove_button_state()
    
    # DTO
    def get_pricebook_config(self, pb_id: str) -> PricebookConfig:
        currencies: list[CurrencyMapping] = []
        for row_widget in self.currency_rows.values():
            currency_data = row_widget.get_currency_settings()
            currencies.append(currency_data)
            
        return PricebookConfig(
            pricebook_id=pb_id,
            currencies=currencies
        )
            
    
    def setup_ui(self, index):
        self.setObjectName(f"currency_tab_{index}")
        self.main_layout = QGridLayout(self)

        # scroll area
        self.scroll = QScrollArea(self)
        self.scroll.setObjectName(f"curr_scroll_area_{index}")
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setWidgetResizable(True) 
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_contents = QWidget()
        self.scroll_contents.setObjectName(f"curr_scroll_area_contents_{index}")

        self.scroll_contents.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )
         
        self.scroll_layout = QGridLayout(self.scroll_contents)

        # frame (curr_frame)
        self.frame = QFrame(self.scroll_contents)
        self.frame.setObjectName(f"curr_frame_{index}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.frame.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        self.frame_layout = QGridLayout(self.frame)

        # headers
        self.header_curr = QLabel("Currency", self.frame)
        self.header_curr.setObjectName(f"header_curr_label_{index}")
        self.header_curr.setAlignment(Qt.AlignCenter)

        self.header_field = QLabel("Input Field", self.frame)
        self.header_field.setObjectName(f"header_field_label_{index}")
        self.header_field.setAlignment(Qt.AlignCenter)

        self.header_cf = QLabel("Conversion Factor", self.frame)
        self.header_cf.setObjectName(f"header_cf_label_{index}")
        self.header_cf.setAlignment(Qt.AlignCenter)

        self.frame_layout.addWidget(self.header_curr, 0, 0)
        self.frame_layout.addWidget(self.header_field, 0, 1)
        self.frame_layout.addWidget(self.header_cf, 0, 2)
        
        self.frame_layout.setColumnStretch(0, 1)
        self.frame_layout.setColumnStretch(1, 1)
        self.frame_layout.setColumnStretch(2, 1)

        # split line
        self.split_line = QFrame(self.frame)
        self.split_line.setObjectName(f"curr_split_line_{index}")
        self.split_line.setFrameShape(QFrame.HLine)
        self.split_line.setFrameShadow(QFrame.Sunken)

        self.frame_layout.addWidget(self.split_line, 1, 0, 1, 3)
        self.frame_layout.setRowStretch(99, 1)


        self.scroll_layout.addWidget(self.frame, 0, 0)
        self.scroll.setWidget(self.scroll_contents)

        self.main_layout.addWidget(self.scroll, 0, 0, 1, 3)
        
        # buttons
        self.add_btn = QPushButton("Add currencies", self)
        self.add_btn.setObjectName(f"add_curr_button_{index}")
        self.add_btn.clicked.connect(self.add_new_currencies)
        
        self.remove_btn = QPushButton("Remove currencies", self)
        self.remove_btn.setEnabled(False)
        self.remove_btn.setObjectName(f"remove_curr_button_{index}")
        self.remove_btn.clicked.connect(self.remove_currencies)
        
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.spacer, 1, 0)
        self.main_layout.addWidget(self.remove_btn, 1, 1)
        self.main_layout.addWidget(self.add_btn, 1, 2)
    

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    currencies = ['EUR', 'PLN', 'USD']
    cols = ['field1', 'f2', 'f3']
    
    app = QApplication(sys.argv)

    window = CurrencyTab(1, currencies, cols)
    window.show()

    sys.exit(app.exec())