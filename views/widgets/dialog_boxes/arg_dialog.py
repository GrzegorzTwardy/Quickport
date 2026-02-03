from PySide6.QtCore import Qt, Signal, QObject, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator, QCloseEvent
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QApplication, QFormLayout,
    QLabel, QLineEdit, QGridLayout, QSizePolicy, 
    QPushButton, QDialog, QComboBox, QFrame)

from exceptions.mapper_exceptions import UnknownMappingTypeError, MappingError

class ArgDialog(QDialog):

    args_saved = Signal(dict)
    canceled = Signal()
    
    def __init__(self, mapping_type: str, sheet_columns: list[str], args_to_load: dict | None, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.args_to_load = args_to_load
        self.saved = False # for "changes will not be saved" pop up 
        
        # DTO
        self.args = {}
        
        self.args_widget = None
        
        self.mapping_type = mapping_type
        self.sheet_columns = sheet_columns
        
        self.setWindowTitle(f'{self.mapping_type} Configuration')
        self.layout = QGridLayout(self)
        self.save_button = QPushButton('Save', self)
        self.back_button = QPushButton('Back', self)
        
        self.connect_signals()
        self.setup_args()
            
        self.layout.addWidget(self.back_button, 1, 0)
        self.layout.addWidget(self.save_button, 1, 1)
        
    
    def closeEvent(self, event: QCloseEvent):
        if self.saved:
            event.accept()
            return

        result = QMessageBox.question(
            self,
            'Cancel Configuration',
            'Are you sure you want to exit without saving changes?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if result == QMessageBox.Yes:
            self.canceled.emit()
            event.accept()
        else:
            event.ignore()

    
    def connect_signals(self):
        self.save_button.clicked.connect(self.get_args_dict)
        self.back_button.clicked.connect(self.close)
            
            
    def get_args_dict(self) -> dict:
        self.args = self.args_widget.get_args_from_ui()
        self.args_saved.emit(self.args)
        self.saved = True
        self.close()
    
    
    def setup_args(self):
        match self.mapping_type:
            case 'SET ALL':
                self.args_widget = SetAllArgs(self.args_to_load, self)
            case 'PRICE':
                self.args_widget = PriceArgs(self.sheet_columns, self.args_to_load, self)
            case 'REPLACE':
                self.args_widget = ReplaceArgs(self.sheet_columns, self.args_to_load, self)
            case 'JOIN':
                self.args_widget = JoinArgs(self.sheet_columns, self.args_to_load, self)
            case _:
                raise UnknownMappingTypeError(f'Uknown mapping type: "{self.mapping_type}"')
        self.layout.addWidget(self.args_widget, 0, 0, 1, 2)

        
    
# ========= utils ===========
def setup_src_column_combo(sheet_columns, combo):
    for i, col in enumerate(sheet_columns):
        combo.addItem(f'{i}: {col}', col)
    combo.setCurrentIndex(0)


def stylize_combo(combo: QComboBox):
    
    def adjust_popup_width(combo: QComboBox):
        fm = combo.fontMetrics()
        max_width = max(
            fm.horizontalAdvance(combo.itemText(i))
            for i in range(combo.count())
        )
        combo.view().setMinimumWidth(max_width + 30)
        
    combo.setMinimumWidth(0)
    combo.setMinimumContentsLength(1)
    combo.setSizeAdjustPolicy(
    QComboBox.AdjustToMinimumContentsLengthWithIcon
    )

    # closed state
    combo.currentTextChanged.connect(
    lambda text, c=combo: c.setToolTip(text)
    )

    # popup
    combo.view().setTextElideMode(Qt.ElideNone)
    adjust_popup_width(combo)
    

def set_combo_index(combo: QComboBox, value: str):  
    for i in range(combo.count()):
        data = combo.itemData(i)
        if data == value:
            combo.setCurrentIndex(i)
            break

# ====================================


# === mapping functions parameters ===

# - set all funtion
class SetAllArgs(QWidget):
    
    def __init__(self, args: dict, parent):
        super().__init__(parent)
        
        self.layout = QFormLayout(self)
        self.layout.setLabelAlignment(Qt.AlignRight)
        
        self.text_label = QLabel(self)
        self.text_label.setText('text value: ')
        
        self.text_le = QLineEdit(self)
        self.text_le.setObjectName('text')
        
        self.layout.addRow(self.text_label, self.text_le)
        
        if args:
            self.fill_ui(args)
            
        self.text_le.setFocus()
        
    
    def fill_ui(self, args: dict):
        self.text_le.setText(args.get('text', ''))
    

    def get_args_from_ui(self):
        return {
            'text': self.text_le.text()
        }
        

# - price funtion
class PriceArgs(QWidget):
    
    def __init__(self, sheet_columns: list[str], args: dict, parent):
        super().__init__(parent)
        
        self.layout = QFormLayout(self)
        self.layout.setLabelAlignment(Qt.AlignRight)
        
        # source column
        self.src_col_label = QLabel(self)
        self.src_col_label.setText('source column: ')      
        self.src_col_combo = QComboBox(self)
        setup_src_column_combo(sheet_columns, self.src_col_combo)
        stylize_combo(self.src_col_combo)
        
        # conversion factor TODO: add "."/"," option
        self.cf_label = QLabel(self)
        self.cf_label.setText('conversion factor: ')       
        self.cf_le = QLineEdit(self)
        self.cf_le.setObjectName('text')
        regex = QRegularExpression(r"^\d+(\.\d{1,2})?$")
        validator = QRegularExpressionValidator(regex, self)
        self.cf_le.setValidator(validator)
        self.cf_le.setText('1.00')
        
        # adding widgets to layout
        self.layout.addRow(self.src_col_label, self.src_col_combo)
        self.layout.addRow(self.cf_label, self.cf_le)
        
        # loading arguments from saved config
        if args:
            self.fill_ui(args)


    def fill_ui(self, args: dict):
        a_src_col = args.get('source_column', '')
        a_cf = args.get('conversion_factor', 1.00)
        set_combo_index(self.src_col_combo, a_src_col)
        self.cf_le.setText(str(a_cf))


    def get_args_from_ui(self):
        # TODO: ADD VALIDATION OF INPUTS
        return {
            'source_column': self.src_col_combo.currentData(),
            'conversion_factor': float(self.cf_le.text()) # add error check?
        }
        

# - replace function
class ReplaceArgs(QWidget):
    
    def __init__(self, sheet_columns: list[str], args: dict | None, parent):
        super().__init__(parent)
        
        self.mapping_rows_count = 0
        self.mapping_rows = [] # api atribute
        
        self.parent = parent
        
        self.layout = QGridLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        
        # source column
        self.src_col_label = QLabel(self)
        self.src_col_label.setText('source column: ')      
        self.src_col_combo = QComboBox(self)
        setup_src_column_combo(sheet_columns, self.src_col_combo)
        stylize_combo(self.src_col_combo)

        # labels
        self.current_value_label = QLabel(self)
        self.current_value_label.setText('Current Value')
        self.current_value_label.setAlignment(Qt.AlignHCenter)
        self.new_value_label = QLabel(self)
        self.new_value_label.setText('New Value')
        self.new_value_label.setAlignment(Qt.AlignHCenter)
        
        # area of mappings
        self.mappings_frame = QFrame(self)
        self.mappings_layout = QGridLayout(self.mappings_frame)
        self.mappings_layout.setContentsMargins(0, 0, 0, 0)
        self.mappings_layout.setAlignment(Qt.AlignTop)
                
        # removing and adding mappings/replacements
        self.remove_last_btn = QPushButton('Remove', self)
        self.add_new_btn = QPushButton('Add', self)
        
        # adding widgets to layout
        self.layout.addWidget(self.src_col_label, 0, 0, 1, 1)
        self.layout.addWidget(self.src_col_combo, 0, 1, 1, 1)
        self.layout.addWidget(self.current_value_label, 1, 0, 1, 1)
        self.layout.addWidget(self.new_value_label, 1, 1, 1, 1)
        self.layout.addWidget(self.mappings_frame, 2, 0, 1, 2)
        self.layout.addWidget(self.remove_last_btn, 3, 0, 1, 1)
        self.layout.addWidget(self.add_new_btn, 3, 1, 1, 1)
        
        # connecting signals
        self.add_new_btn.clicked.connect(lambda: self.add_mapping_row(None))
        self.remove_last_btn.clicked.connect(self.remove_last_row)
        
        if args:
            self.fill_ui(args) # loading arguments from saved config
        else:
            self.add_mapping_row(None) # initial 1st row
        
        # disabling widgets
        self.remove_last_btn.setEnabled(self.mapping_rows_count > 1)


    def add_mapping_row(self, value_pair: tuple[str, str] | None):
        current_le = QLineEdit(self.mappings_frame)
        new_le = QLineEdit(self.mappings_frame)

        if value_pair:
            current_le.setText(value_pair[0])
            new_le.setText(value_pair[1])

        # adding rows to api atribute
        self.mapping_rows.append((current_le, new_le))
        
        row = self.mapping_rows_count

        self.mappings_layout.addWidget(current_le, row, 0)
        self.mappings_layout.addWidget(new_le, row, 1)

        self.mappings_layout.setColumnStretch(0, 1)
        self.mappings_layout.setColumnStretch(1, 1)

        self.mapping_rows_count += 1

        if self.parent:
            QApplication.processEvents() 
            self.adjustSize()
            
        self.remove_last_btn.setEnabled(True)


    def remove_last_row(self):
        if self.mapping_rows_count <= 1:
            return

        last_row = self.mapping_rows_count - 1

        # Removing widgets from layout
        for col in range(2):
            item = self.mappings_layout.itemAtPosition(last_row, col)
            if not item:
                continue

            widget = item.widget()
            self.mappings_layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()

        # removing last row from api atribute
        if self.mapping_rows:
            self.mapping_rows.pop()

        self.mapping_rows_count -= 1
        self.remove_last_btn.setEnabled(self.mapping_rows_count > 1)

        self.adjustSize()
        if self.parent:
            self.parent.adjustSize()


    def fill_ui(self, args: dict):
        a_src_col = args.get('source_column', '')
        a_value_mappings = args.get('value_mapping', {})
        
        set_combo_index(self.src_col_combo, a_src_col)

        for current_v, new_v in a_value_mappings.items():
            self.add_mapping_row((current_v, new_v))
        
        if self.mapping_rows_count == 0:
            self.add_mapping_row(None)
        

    def get_args_from_ui(self):
        # TODO: ADD VALIDATION OF INPUTS
        value_mapping = {}
        
        for mapping in self.mapping_rows:
            current_value = mapping[0].text()
            new_value = mapping[1].text()
            
            if not current_value:
                continue

            value_mapping[current_value] = new_value
        
        return {
            'source_column': self.src_col_combo.currentData(),
            'value_mapping': value_mapping
        }


# - join function
class JoinArgs(QWidget):
    
    def __init__(self, sheet_columns: list[str], args: dict | None, parent):
        super().__init__(parent)
        
        self.join_rows_count = 0
        self.join_rows = [] # api atribute
        self.sheet_columns = sheet_columns
        
        self.parent = parent
        
        self.layout = QGridLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        
        # separator and null display config
        self.separator_label = QLabel(self)
        self.separator_label.setText('sepataror: ')
        self.separator_label.setAlignment(Qt.AlignRight)
        self.separator_le = QLineEdit(self)
        self.separator_le.setText('-')
        
        self.null_display_label = QLabel(self)
        self.null_display_label.setText('null display: ')
        self.null_display_label.setAlignment(Qt.AlignRight)
        self.null_display_le = QLineEdit(self)
        self.null_display_le.setText('null')
        
        # removing and adding joins
        self.remove_last_btn = QPushButton('Remove', self)
        self.add_new_btn = QPushButton('Add', self)      

        # labels
        self.src_cols_label = QLabel(self)
        self.src_cols_label.setText('Add columns to join:')
        
        # area of joins
        self.join_frame = QFrame(self)
        self.join_layout = QGridLayout(self.join_frame)
        self.join_layout.setContentsMargins(0, 0, 0, 0)
        self.join_layout.setAlignment(Qt.AlignTop)
                
        # adding widgets to layout
        self.layout.addWidget(self.remove_last_btn, 0, 0, 1, 1)
        self.layout.addWidget(self.add_new_btn, 0, 1, 1, 1)
        self.layout.addWidget(self.separator_label, 1, 0, 1, 1)
        self.layout.addWidget(self.separator_le, 1, 1, 1, 1)
        self.layout.addWidget(self.null_display_label, 2, 0, 1, 1)
        self.layout.addWidget(self.null_display_le, 2, 1, 1, 1)
        self.layout.addWidget(self.src_cols_label, 3, 0, 1, 2)
        self.layout.addWidget(self.join_frame, 4, 0, 1, 2)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        
        # connecting signals
        self.add_new_btn.clicked.connect(lambda: self.add_join_row(None))
        self.remove_last_btn.clicked.connect(self.remove_last_row)
        
        if args:
            self.fill_ui(args) # loading arguments from saved config
        else:
            self.add_join_row(None) # initial 1st row
            self.add_join_row(None) # initial 2nd row
        
        # disabling widgets
        self.remove_last_btn.setEnabled(self.join_rows_count > 2)
        self.separator_le.setFocus()


    def add_join_row(self, current_data):
        combo = QComboBox(self.join_frame)
        setup_src_column_combo(self.sheet_columns, combo)
        stylize_combo(combo)
        if current_data:
            set_combo_index(combo, current_data)
        
        self.join_rows.append(combo)
        
        row = self.join_rows_count
        
        self.join_layout.addWidget(combo, row, 0)

        self.join_rows_count += 1

        if self.parent:
            QApplication.processEvents() 
            self.adjustSize()
            
        self.remove_last_btn.setEnabled(True)


    def remove_last_row(self):
        if self.join_rows_count <= 1:
            return

        last_row = self.join_rows_count - 1

        # Removing widgets from layout
        for col in range(2):
            item = self.join_layout.itemAtPosition(last_row, col)
            if not item:
                continue

            widget = item.widget()
            self.join_layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()

        # removing last row from api atribute
        if self.join_rows:
            self.join_rows.pop()

        self.join_rows_count -= 1
        self.remove_last_btn.setEnabled(self.join_rows_count > 2)

        self.adjustSize()
        if self.parent:
            self.parent.adjustSize()


    def fill_ui(self, args: dict):
        a_src_cols = args.get('source_columns', '')
        a_separator = args.get('separator', '-')
        a_null_display = args.get('null_display', 'null')

        self.separator_le.setText(a_separator)
        self.null_display_le.setText(a_null_display)

        for combo_data in a_src_cols:
            self.add_join_row(combo_data)
        
        # if args.source_columns is empty we add an empty row combo
        if self.join_rows_count == 0:
            self.add_join_row(None)
            self.add_join_row(None)
        

    def get_args_from_ui(self):
        # TODO: ADD VALIDATION OF INPUTS
        src_columns = []
        separator = self.separator_le.text() if self.separator_le.text() else '-'
        null_display = self.null_display_le.text() if self.null_display_le.text() else 'null'
        
        for combo in self.join_rows:
            src_columns.append(combo.currentData())
            
        return {
            'source_columns': src_columns,
            'separator': separator,
            'null_display': null_display
        }

        
        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QWidget, QGridLayout
    from views.widgets.product2_row import Product2Row

    app = QApplication(sys.argv)
    
    window = QWidget()
    layout = QGridLayout()
    window.setLayout(layout)
    
    row = Product2Row('sf_field', { 'required': 'True', 'readOnly':'false' }, ['field1', 'field2'], None)
    
    layout.addWidget(row.include_checkbox, 0, 0) 
    layout.addWidget(row.name_label, 0, 1) 
    layout.addWidget(row.field_combo, 0, 2) 
    layout.addWidget(row.function_combo, 0, 3) 
    layout.addWidget(row.allow_nulls_checkbox, 0, 4)
    
    window.show()

    sys.exit(app.exec())
