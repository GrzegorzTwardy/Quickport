from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import (
    QLabel, QGridLayout, QWidget,
    QCheckBox, QComboBox, QSizePolicy
)

from core.mapper.mapper_model import ProductFieldMapping
from core.mapper.mapper_functions import mapping_functions_list
from views.widgets.utils.hover_label import HoverLabel
from exceptions.gui_exceptions import MappingNotSetError

# TODO: WYŚWIETLANIE OKNA DLA ARGS DLA FUNCTION COMBO
class Product2Row(QObject):

    def __init__(self, field_name: str, field_metadata: dict, sheet_columns: list[str], parent=None):
        super().__init__(parent)
        
        self.field_name = field_name
        self.field_metadata = field_metadata
        self.sheet_columns = sheet_columns
        
        # TODO: add more functions
        self.functions = mapping_functions_list.copy()
        
        self.create_widgets(parent)
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


    def create_widgets(self, parent):
        checkbox_size_policy = QSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Fixed
        )

        self.include_checkbox = QCheckBox(parent)
        self.include_checkbox.setChecked(True)
        self.include_checkbox.setSizePolicy(checkbox_size_policy)

        # OLD vanilla label with max text length
        max_label_name = 16
        # self.name_label = QLabel(self.format_field_name(self.field_name, max_label_name), self)
        # if len(self.name_label.text()) == max_label_name + 3: # '...'
        #     self.name_label.setToolTip(self.field_name)
        self.name_label = HoverLabel(
            self.format_field_name(self.field_name, max_label_name),
            self.field_metadata,
            parent
        )

        self.field_combo = QComboBox(parent)
        self.field_combo.addItem('...', None)
        for i, col in enumerate(self.sheet_columns):
            self.field_combo.addItem(f'{i}: {col}', col)
        self.field_combo.setCurrentIndex(0)
        

        self.function_combo = QComboBox(parent)
        # TODO: add functions from available transformations
        self.function_combo.addItem('...', None)
        for f in self.functions:
            self.function_combo.addItem(f, f)
        self.function_combo.setCurrentIndex(0)

        self.allow_nulls_checkbox = QCheckBox(parent)
        self.allow_nulls_checkbox.setSizePolicy(checkbox_size_policy)
            
        for combo in (self.field_combo, self.function_combo):
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

    
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    from threading import Timer

    app = QApplication(sys.argv)

    window = Product2Row('sf_field', { 'required': 'True', 'readOnly':'false' }, ['field1', 'field2'], None)
    window.show()

    sys.exit(app.exec())
