from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtGui import QIcon

import json
from pathlib import Path

from ui.ui_mapper_list import Ui_MapperListMain
from dtos.session import AppSession


class MapperListWindow(QWidget):
    
    PATH_TO_MAPPERS = Path('./mappers/')
    
    def __init__(self, session: AppSession, mapper_config=None):
        super().__init__()
        self.ui = Ui_MapperListMain()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon())
        
        self.available_mappers = []
        
        self.loadMappers()
        
    def loadMappers(self):
        for json_file in self.PATH_TO_MAPPERS.glob('*.json'):
            with open(json_file, 'r', encoding='utf-8') as file:
                mapper = json.load(file)
                self.available_mappers.append(mapper)    
            mapper_name = json_file.stem
            self.ui.mapperList.addItem(mapper_name)
        
        
        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    session = AppSession()
    session.test_login()

    window = MapperListWindow(None, None)
    window.show()

    sys.exit(app.exec())