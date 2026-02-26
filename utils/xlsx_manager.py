import pandas as pd
from pathlib import Path
from PySide6 import QtCore
from datetime import datetime


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


def dict_to_xlsx(obj: dict | list, file_path: str, use_date: bool = False):
    if use_date:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = Path(file_path)
        new_filename = f"{path.stem}_{current_time}{path.suffix}"
        file_path = path.with_name(new_filename)
        
    df = pd.DataFrame(obj)
    df.to_excel(file_path, index=False)

    
if __name__ == "__main__":
    file_path = Path('./data/ab.xlsx')
    pricebooks = get_sheets_from_file(file_path)
    print(pricebooks)