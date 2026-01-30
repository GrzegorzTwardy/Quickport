from PySide6.QtCore import Qt, Signal, QObject, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QApplication, QFormLayout,
    QLabel, QLineEdit, QGridLayout, 
    QPushButton, QDialog, QComboBox)

from exceptions.mapper_exceptions import UnknownMappingTypeError, MappingError

class ArgDialog(QDialog):

    args_saved = Signal(dict)
    canceled = Signal()
    
    def __init__(self, mapping_type: str, sheet_columns: list[str], args_to_load: dict | None, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.args_to_load = args_to_load
        
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
        
        
    def connect_signals(self):
        self.save_button.clicked.connect(self.get_args_dict)
        self.back_button.clicked.connect(self.closing_confirmation)
    
    
    def closing_confirmation(self):
        result = QMessageBox.question(
            None,
            'Cancel Configuration',
            'Are you sure you want to exit without saving changes?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if result == QMessageBox.Yes:
            self.canceled.emit()
            self.close()
            
            
    def get_args_dict(self) -> dict:
        self.args = self.args_widget.get_args_from_ui()
        self.args_saved.emit(self.args)
        self.close()
    
    
    def setup_args(self):
        # TODO: wiecej funckji
        match self.mapping_type:
            case 'SET ALL':
                self.args_widget = SetAllArgs(self.args_to_load, self)
            case 'PRICE':
                self.args_widget = PriceArgs(self.sheet_columns, self.args_to_load, self)
            case 'REPLACE':
                self.args_widget = ReplaceArgs(self.sheet_columns, self.args_to_load, self)
            case _:
                raise UnknownMappingTypeError(f'Uknown mapping type: "{self.mapping_type}"')
        self.layout.addWidget(self.args_widget, 0, 0, 1, 2)  

        
    
# ========= utils ===========
def setup_src_column_combo(sheet_columns, combo):
    combo.addItem('...', None)
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
# ====================================


# === mapping functions parameters ===

# - set all funtion
class SetAllArgs(QWidget):
    
    def __init__(self, args: dict, parent):
        super().__init__(parent)
        
        layout = QFormLayout(self)
        layout.setLabelAlignment(Qt.AlignRight)
        
        self.text_label = QLabel(self)
        self.text_label.setText('text value: ')
        
        self.text_le = QLineEdit(self)
        self.text_le.setObjectName('text')
        
        layout.addRow(self.text_label, self.text_le)
        
        if args:
            self.fill_ui(args)

    
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
        
        layout = QFormLayout(self)
        layout.setLabelAlignment(Qt.AlignRight)
        
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
        layout.addRow(self.src_col_label, self.src_col_combo)
        layout.addRow(self.cf_label, self.cf_le)
        
        # loading arguments from saved config
        if args:
            self.fill_ui(args)


    def fill_ui(self, args: dict):
        a_src_col = args.get('source_column', '')
        a_cf = args.get('conversion_factor', 1.00)
        
        for i in range(self.src_col_combo.count()):
            data = self.src_col_combo.itemData(i)
            if data == a_src_col:
                self.src_col_combo.setCurrentIndex(i)
                break
        self.cf_le.setText(str(a_cf))


    def get_args_from_ui(self):
        # TODO: ADD VALIDATION OF INPUTS
        return {
            'source_column': self.src_col_combo.currentData(),
            'conversion_factor': float(self.cf_le.text()) # add error check?
        }
        

# - replace function
class ReplaceArgs(QWidget):
    
    def __init__(self, sheet_columns: list[str], args: dict, parent):
        super().__init__(parent)
        
        layout = QFormLayout(self)
        layout.setLabelAlignment(Qt.AlignRight)
        
        # source column
        self.src_col_label = QLabel(self)
        self.src_col_label.setText('source column: ')      
        self.src_col_combo = QComboBox(self)
        setup_src_column_combo(sheet_columns, self.src_col_combo)
        stylize_combo(self.src_col_combo)
        
        # current value
        self.current_value_label = QLabel(self)
        self.current_value_label.setText('current value: ')
        self.current_le = QLineEdit(self)
        
        # new value
        self.new_value_label = QLabel(self)
        self.new_value_label.setText('new value: ') 
        self.new_le = QLineEdit(self)
        
        # adding widgets to layout
        layout.addRow(self.src_col_label, self.src_col_combo)
        layout.addRow(self.current_value_label, self.current_le)
        layout.addRow(self.new_value_label, self.new_le)
        
        # loading arguments from saved config
        if args:
            self.fill_ui(args)


    def fill_ui(self, args: dict):
        pass


    def get_args_from_ui(self):
        # TODO: ADD VALIDATION OF INPUTS
        pass

        
        
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
