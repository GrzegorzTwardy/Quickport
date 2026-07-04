from PySide6.QtCore import (Qt, Signal, QRegularExpression)
from PySide6.QtGui import QDoubleValidator, QRegularExpressionValidator
from PySide6.QtWidgets import (
    QLabel, QGridLayout, QWidget, QComboBox, QLineEdit, QSizePolicy
)

from core.mapper.mapper_model import CurrencyMapping
from utils.convert_to_valid_price import convert_to_valid_price
from exceptions.gui_exceptions import MappingNotSetError

class CurrencyRow(QWidget):

    row_changed = Signal()

    def __init__(
        self, 
        currency_code, 
        sheet_columns, 
        currency_mapping: CurrencyMapping | None, 
        parent=None, 
        parent_layout=None
    ):
        super().__init__(parent)
        
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        
        self.currency_code = currency_code
        self.sheet_columns = sheet_columns
        self.currency_mapping = currency_mapping

        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        if parent_layout:
            layout.setSpacing(parent_layout.spacing())

        self.curr_label = QLabel(currency_code, self)
        self.curr_label.setAlignment(Qt.AlignCenter)

        self.curr_field_combo = QComboBox(self)
        self.curr_field_combo.addItem('...', None)
        
        for i, col in enumerate(self.sheet_columns):
            self.curr_field_combo.addItem(f'{i}: {col}', col)
        self.curr_field_combo.setCurrentIndex(0)

        regex = QRegularExpression(r"^\d+([.,]\d{1,10})?$")
        validator = QRegularExpressionValidator(regex, self)
        
        self.c_factor_ledit = QLineEdit('1.00', self)
        self.c_factor_ledit.setValidator(validator)
        
        self.c_factor_ledit.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        self.c_factor_ledit.setMinimumWidth(0)
        self.c_factor_ledit.editingFinished.connect(self.autocorrect_price)
            
        self.curr_field_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.curr_field_combo.setMinimumWidth(0)
        self.curr_field_combo.setMinimumContentsLength(1)
        self.curr_field_combo.setSizeAdjustPolicy(
            QComboBox.AdjustToMinimumContentsLengthWithIcon
        )
        self.curr_field_combo.view().setTextElideMode(Qt.ElideRight)
        
        # closed state
        self.curr_field_combo.currentTextChanged.connect(
            lambda text, c=self.curr_field_combo: c.setToolTip(text)
        )

        # popup
        self.curr_field_combo.view().setTextElideMode(Qt.ElideNone)
        self.adjust_popup_width(self.curr_field_combo)
        
        layout.addWidget(self.curr_label, 0, 0)
        layout.addWidget(self.curr_field_combo, 0, 1)
        # layout.addWidget(self.function_combo, 0, 2)
        layout.addWidget(self.c_factor_ledit, 0, 2)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 2)
        
        # signaling changes
        self.curr_field_combo.currentIndexChanged.connect(lambda *args: self.row_changed.emit())
        self.c_factor_ledit.editingFinished.connect(lambda *args: self.row_changed.emit())

        if self.currency_mapping is not None:
            self.load_mapping()


    def autocorrect_price(self):
        current_text = self.c_factor_ledit.text()
        valid_price = convert_to_valid_price(current_text)

        if valid_price:
            self.c_factor_ledit.setText(str(valid_price))

    
    def load_mapping(self):
        source_column = self.currency_mapping.source_column
        index = self.curr_field_combo.findData(source_column)
        cf = self.currency_mapping.conversion_factor
        
        if index != -1: 
            self.curr_field_combo.setCurrentIndex(index)
        self.c_factor_ledit.setText(str(cf))
        
        
    def adjust_popup_width(self, combo):
        fm = combo.fontMetrics()
        
        if combo.count() == 0:
            if combo == self.curr_field_combo:
                raise ValueError('No input fields detected')
            else:
                raise ValueError('Error while loading functions')
        
        max_width = max(
            fm.horizontalAdvance(combo.itemText(i))
            for i in range(combo.count())
        )
        combo.view().setMinimumWidth(max_width + 30)
        

    # DTO
    def get_currency_settings(self) -> CurrencyMapping:
        source_col = self.curr_field_combo.currentData()
        
        if source_col is None:
            raise MappingNotSetError(self.currency_code)
        
        return CurrencyMapping(
            code=self.currency_code,
            source_column=source_col,
            conversion_factor=float(self.c_factor_ledit.text())
        )

    
if __name__ == "__main__":
    
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = CurrencyRow('EUR', ['field1', 'field2'], None)
    window.show()

    sys.exit(app.exec())
