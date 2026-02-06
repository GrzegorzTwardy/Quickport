from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import (
    QLabel, QGridLayout,
    QCheckBox, QComboBox, QSizePolicy
)

from core.mapper.mapper_model import ProductFieldMapping
from core.mapper.mapper_functions import mapping_functions_list
from views.widgets.utils.hover_label import HoverLabel
from views.widgets.dialog_boxes.arg_dialog import ArgDialog
from views.widgets.utils.no_scroll_combo_box import NoScrollComboBox
from exceptions.gui_exceptions import MappingNotSetError


# TODO: 
# - display mapping args while hovering over function combo
# - when mapping function is chosen from combo display sf_field hint

class Product2Row(QObject):

    def __init__(
        self, 
        field_name: str, 
        field_metadata: dict, 
        sheet_columns: list[str], 
        field_mapping: ProductFieldMapping | None,
        parent=None
    ):
        super().__init__(parent)
        
        self.mapping_args = {}
        self.last_saved_mapping: str | None = None 
        
        self.field_name = field_name
        self.field_metadata = field_metadata
        self.sheet_columns = sheet_columns
        self.field_mapping = field_mapping
        
        self.functions = mapping_functions_list.copy()
        
        self.create_widgets(parent)
        self.connect_signals()
        
        if self.field_mapping is not None:
            self.load_mapping()
            # self.update_combos()

        
    def connect_signals(self):
        self.field_combo.currentIndexChanged.connect(self.update_combos)
        self.function_combo.currentIndexChanged.connect(self.update_combos)
        self.function_combo.activated.connect(self.on_function_selected)
        self.include_checkbox.checkStateChanged.connect(self.change_row_state)
           
    
    def load_mapping(self):
        if not self.field_mapping.included:
            self.include_checkbox.setChecked(False)
            
        if self.field_mapping.source_column is not None:
            source_column = self.field_mapping.source_column
            index = self.field_combo.findData(source_column)
            if index != -1: 
                self.field_combo.setCurrentIndex(index)
        elif self.field_mapping.mapping_type is not None:
            mapping_type = self.field_mapping.mapping_type
            index = self.function_combo.findData(mapping_type)
            if index != -1: 
                self.function_combo.setCurrentIndex(index)
                self.mapping_args = self.field_mapping.args if self.field_mapping.args else {}
                self.last_saved_mapping = mapping_type
            
        if self.field_mapping.allows_nulls:
            self.allow_nulls_checkbox.setChecked(True)
        self.update_combos()
    
       
    def adjust_popup_width(self, combo):
        fm = combo.fontMetrics()
        max_width = max(
            fm.horizontalAdvance(combo.itemText(i))
            for i in range(combo.count())
        )
        combo.view().setMinimumWidth(max_width + 30)


    def update_combos(self):
        event_combo = self.sender()
        
        if event_combo is None: # manual invoke (for editing mapper)
            if self.field_combo.currentData() is not None:
                self.function_combo.setEnabled(False)
                self.field_combo.setEnabled(True)
            elif self.function_combo.currentData() is not None:
                self.field_combo.setEnabled(False)
                self.function_combo.setEnabled(True)
            else:
                self.field_combo.setEnabled(True)
                self.function_combo.setEnabled(True)
            return
        
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
            mapping_type=mapping_type,
            allows_nulls=self.allow_nulls_checkbox.isChecked(),
            args=self.mapping_args
        )


    # === setting up arg window ===        
    def open_arg_window(self, mapping_name):
        
        def _save_args(args):
            self.mapping_args = args
            self.last_saved_mapping = mapping_name
            
        def _on_canceled():
            if mapping_name != self.last_saved_mapping:
                index = self.function_combo.findData(None)
                if index != -1:
                    self.function_combo.setCurrentIndex(index)
        
        # check if the same mapping is used again, if so then load saved arg config
        if mapping_name == self.last_saved_mapping:      
            self._arg_window = ArgDialog(mapping_name, self.sheet_columns, self.mapping_args)
        else:
            self._arg_window = ArgDialog(mapping_name, self.sheet_columns, None)
            
        self._arg_window.args_saved.connect(_save_args)
        self._arg_window.canceled.connect(_on_canceled)
        self._arg_window.show()
        self._arg_window.raise_()
        self._arg_window.activateWindow()
   
        
    def on_function_selected(self, index: int):
        mapping_name = self.function_combo.itemData(index)
        if mapping_name is None:
            return
        self.open_arg_window(mapping_name)
    # =============================
    

    def create_widgets(self, parent):
        checkbox_size_policy = QSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Fixed
        )

        self.include_checkbox = QCheckBox(parent)
        self.include_checkbox.setChecked(True)
        self.include_checkbox.setSizePolicy(checkbox_size_policy)

        max_label_name = 16
        self.name_label = None
        
        if self.field_metadata is None:
            self.name_label = HoverLabel(
                self.format_field_name(self.field_name, max_label_name),
                { 'Error': 'Field missing in Salesforce.' },
                parent
            )
            self.name_label.setStyleSheet('color: red;') # red if field is missing from Salesforce
        else:
            self.name_label = HoverLabel(
                self.format_field_name(self.field_name, max_label_name),
                self.field_metadata,
                parent
            )

        self.field_combo = QComboBox(parent)
        self.field_combo.addItem('...', None)
        
        # if self.df_column_amount is not None: 
        #     snapshot_cols_count = len(self.sheet_columns) - self.df_column_amount
            
        #     if snapshot_cols_count < 0:
        #         raise ValueError('An error occured while calculating available columns.')
                
        #     for i, col in enumerate(self.sheet_columns):
        #         if i < snapshot_cols_count:
        #             self.field_combo.addItem(f'{i} (Saved in Mapper): {col}', col)
        #         else:
        #             self.field_combo.addItem(f'{i}: {col}', col)
        # else:
        #     for i, col in enumerate(self.sheet_columns):
        #         self.field_combo.addItem(f'{i}: {col}', col)
        for i, col in enumerate(self.sheet_columns):
            self.field_combo.addItem(f'{i}: {col}', col)
            
        self.field_combo.setCurrentIndex(0)
        
        self.function_combo = NoScrollComboBox(parent)
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
    from PySide6.QtWidgets import QApplication, QWidget, QGridLayout

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
