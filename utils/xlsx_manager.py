import pandas as pd
from pathlib import Path
from PySide6 import QtCore


def get_sheets_from_file(xlsx_path: Path | str) -> dict[str, pd.DataFrame]:
    raw_sheets = pd.read_excel(xlsx_path, sheet_name=None, header=None)
    dfs: dict[str, pd.DataFrame] = {}

    for sheet_name, df in raw_sheets.items():
        processed_df = process_sheet(df)
        dfs[sheet_name] = processed_df
        
    return dfs
    

def process_sheet(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")

    df = df.reset_index(drop=True)

    if df.empty:
        return df
    
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)

    return df


# def populate_qtable(self):

#     df_model = QtCore.QAbstractTableModel()
    
#     def __init__(self, data, parent=None):
#         super().__init__(parent)
#         self._data = data

#     def rowCount(self, parent=None):
#         return len(self._data.values)

#     def columnCount(self, parent=None):
#         return self._data.columns.size

#     def data(self, index, role=QtCore.Qt.DisplayRole):
#         if index.isValid():
#             if role == QtCore.Qt.DisplayRole:
#                 return str(self._data.iloc[index.row()][index.column()])
#         return None

#     def headerData(self, col, orientation, role):
#         if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
#             return self._data.columns[col]
#         return None

    
if __name__ == "__main__":
    file_path = Path('./data/ab.xlsx')
    pricebooks = get_sheets_from_file(file_path)
    print(pricebooks)