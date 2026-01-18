from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QGridLayout, QTableWidget, QTableWidgetItem,
    QWidget)

import pandas as pd


class TableTab(QWidget):
    
    def __init__(self, sheet_name: str, df: pd.DataFrame | None, parent=None):
        super().__init__(parent)
        self.df = df
        self.sheet_name = sheet_name
        
        self.setup_ui()
        
        if self.sheet_name == 'Product2 Preview':
            self.setup_product2_table()
        else:
            self.setup_file_preview_table()
        
        
    def setup_ui(self):
        self.gridLayout = QGridLayout(self)
        self.table = QTableWidget(self)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
    
    
    def setup_product2_table(self):
        pass
    
    
    def setup_file_preview_table(self):
        self.populate_table_widget(self.table, self.df)
    
    
    def populate_table_widget(self, table, df):
        # Set dimensions
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))

        indexed_cols = [f'{i}: {col}' for i, col in enumerate(df.columns)]

        # Set headers
        # table.setHorizontalHeaderLabels(df.columns.astype(str).tolist())
        table.setHorizontalHeaderLabels(indexed_cols)

        # Fill table
        for row in range(len(df)):
            for col in range(len(df.columns)):
                value = df.iat[row, col]
                item = QTableWidgetItem(str(value))

                # Optional: align numbers to the right
                if isinstance(value, (int, float)):
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                table.setItem(row, col, item)


if __name__ == '__main__':
    import sys
    from pathlib import Path
    from utils.xlsx_manager import get_sheets_from_file
    
    file_path = Path('./data/ab.xlsx')
    dfs = get_sheets_from_file(file_path)
    
    app = QApplication(sys.argv)
    tab = TableTab('name', dfs['renewals'])
    tab.show()
    sys.exit(app.exec())