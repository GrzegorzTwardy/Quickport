from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel, QGridLayout, QWidget,
    QCheckBox, QComboBox, QSizePolicy
)

from core.mapper.mapper_model import ProductFieldMapping

from exceptions.gui_exceptions import MappingNotSetError

class Product2Row(QWidget):

    def __init__(self, field_name: str, sheet_columns: list[str], parent=None):
        super().__init__(parent)
        
        self.field_name = field_name
        self.sheet_columns = sheet_columns
        # TODO: get functions from file
        self.functions = ['SPLIT', 'PRICE', 'FUNCTION']
        
        self.setup_ui()
        self.connect_signals()

        
    def connect_signals(self):
        self.field_combo.currentIndexChanged.connect(self.update_combos)
        self.function_combo.currentIndexChanged.connect(self.update_combos)
        self.include_checkbox.checkStateChanged.connect(self.change_row_state)
           
           
    def adjust_popup_width(self, combo):
        fm = combo.fontMetrics()
        max_width = max(
            fm.horizontalAdvance(combo.itemText(i))
            for i in range(combo.count())
        )
        combo.view().setMinimumWidth(max_width + 30)


    def update_combos(self):
        event_combo = self.sender()
        other_combo = (
            self.function_combo
            if event_combo == self.field_combo
            else self.field_combo
        )
        other_combo.setEnabled(event_combo.currentData() is None)


    def change_row_state(self):
        # disabling widgets
        row_widgets = [
            self.name_label,
            self.field_combo,
            self.function_combo,
            self.allow_nulls_checkbox
        ]
        
        is_enabled = self.include_checkbox.isChecked()
        for w in row_widgets:
            w.setEnabled(is_enabled)


    def format_field_name(self, name: str, max_len: int):
        if len(name) > max_len:
            return name[:max_len] + '...'
        return name

    # DTO
    def get_product2_mapping(self) -> ProductFieldMapping | None:    
        source_column = self.field_combo.currentData()
        mapping_type = self.function_combo.currentData()
        
        # if both options are empty '...'
        if self.include_checkbox.isChecked() and source_column is None and mapping_type is None:
            raise MappingNotSetError(self.field_name)
        
        return ProductFieldMapping(
            included=self.include_checkbox.isChecked(),
            sf_target_field=self.field_name,
            source_column=source_column,
            mapping_type=mapping_type, # TODO: to bedzie to zmiany po implementowaniu funkcji tranformacji
            allows_nulls=self.allow_nulls_checkbox.isChecked()
        )


    def setup_ui(self):
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )
        
        checkbox_size_policy = QSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Fixed
        )
        
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.include_checkbox = QCheckBox(self)
        self.include_checkbox.setChecked(True)
        self.include_checkbox.setSizePolicy(checkbox_size_policy)

        max_label_name = 8
        self.name_label = QLabel(self.format_field_name(self.field_name, max_label_name), self)
        if len(self.name_label.text()) == max_label_name + 3: # '...'
            self.name_label.setToolTip(self.field_name)

        self.field_combo = QComboBox(self)
        self.field_combo.addItem('...', None)
        for i, col in enumerate(self.sheet_columns):
            self.field_combo.addItem(f'{i}: {col}', col)
        self.field_combo.setCurrentIndex(0)
        

        self.function_combo = QComboBox(self)
        # TODO: add functions from available transformations
        self.function_combo.addItem('...', None)
        for f in self.functions:
            self.function_combo.addItem(f, f)
        self.function_combo.setCurrentIndex(0)

        self.allow_nulls_checkbox = QCheckBox(self)
        self.allow_nulls_checkbox.setSizePolicy(checkbox_size_policy)
            
        for combo in (self.field_combo, self.function_combo):
            # combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
            self.adjust_popup_width(combo)

        layout.addWidget(self.include_checkbox, 0, 0)
        layout.addWidget(self.name_label, 0, 1)
        layout.addWidget(self.field_combo, 0, 2)
        layout.addWidget(self.function_combo, 0, 3)
        layout.addWidget(self.allow_nulls_checkbox, 0, 4)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 2)
        layout.setColumnStretch(4, 2)

    
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    from threading import Timer

    app = QApplication(sys.argv)

    window = Product2Row('sf_field', ['field1', 'field2'], None)
    window.show()

    sys.exit(app.exec())
