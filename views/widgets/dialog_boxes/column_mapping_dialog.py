from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QComboBox, QDialogButtonBox, QScrollArea, QWidget, QFormLayout
)
from PySide6.QtCore import Qt


class ColumnMappingDialog(QDialog):
    def __init__(self, required_columns: list[str], available_columns: list[str], sheet_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'Mapping columns - {sheet_name}')
        self.resize(400, 500)
        
        self.mapping_result = {}
        self.combos = {}
        
        layout = QVBoxLayout(self)
        
        info_label = QLabel(
            f"Mapper expects specific column names in '{sheet_name}' spreadsheet.\n"
            'Map the columns from your file to the names in Mapper.'
        )
        layout.addWidget(info_label)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        self.form_layout = QFormLayout(content_widget)
        
        for req_col in required_columns:
            combo = QComboBox()
            combo.addItem('--- Skip / Missing from file ---', None)
            
            for excel_col in available_columns:
                combo.addItem(excel_col, excel_col)
            
            index = combo.findData(req_col)
            if index != -1:
                combo.setCurrentIndex(index)
            
            self.combos[req_col] = combo
            self.form_layout.addRow(f'{req_col}  →', combo)
            
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)


    def get_mapping(self) -> dict[str, str]:
        rename_dict = {}
        for req_col, combo in self.combos.items():
            selected_excel_col = combo.currentData()
            if selected_excel_col:
                rename_dict[selected_excel_col] = req_col
        return rename_dict
    
    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = ColumnMappingDialog(['a', 'b', 'c'], ['1', '2', '3'], 'sheet1')
    window.show()

    sys.exit(app.exec())