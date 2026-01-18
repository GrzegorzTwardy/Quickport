from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget, QCheckBox, QComboBox, QMessageBox)

from ui.ui_parser_editor import Ui_ParserEditor
from core.mapper_manager import ParserManager
# TODO: load engine.py
from views.widgets.currency_tab import CurrencyTab


class ParserEditorWindow(QWidget):
    
    def __init__(self, parser_config=None):
        super().__init__()
        self.ui = Ui_ParserEditor()
        self.ui.setupUi(self)

        # GLOBAL VALUES
        self.pricebook_counter = 0
        self.currency_tab_next_id = 0
        self.all_currency_tabs = {}
    
        # data for testing
        self.user_sf_data = {
            'pricebooks': ['pb-1', 'pb-2', 'pb-3', 'new_pb_1'],
            'available_currencies': ['EUR', 'PLN', 'USD', 'CZK'],
            'product2_fields': [f'sf_{f}' for f in ['id', 'name', 'SKU', 'manu', 'category', 'desc']]
        }

        # ==== SETTING UP PARSER ====
        self.setup_empty_parser()
        
        # ==== LOADING CONFIG (if editing existing parser) ====
        if parser_config:
            self.load_parser_config()
        

    def _connect_signals(self):
        self.ui.pb_searchbar_line_edit.textChanged.connect(self.setup_pricebook_search)
        self.ui.pricebooks_list.itemChanged.connect(self.update_currency_tabs)
                
                 
    def load_pricebooks_TEST(self):
        for i, pb in enumerate(self.user_sf_data['pricebooks']):
            item = QListWidgetItem(pb)

            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)

            self.ui.pricebooks_list.addItem(item)

            if i == 0:
                self.ui.pricebooks_list.setCurrentItem(item)


    def load_product2_fields_TEST(self):
        pass


    def setup_pricebook_search(self, text):
        for i in range(self.ui.pricebooks_list.count()):
            item = self.ui.pricebooks_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())
    
    # ==== SETTING UP EMPTY PARSER=====
    def setup_empty_parser(self):
        self._connect_signals()
        # TODO: sf_api.connect_to_salesforce()
        self.load_pricebooks_TEST()
        self.create_currency_tabs()
        self.update_currency_tabs()
        self.load_product2_fields_TEST()
    
    
    # ==== EDITING EXISTING PARSER =====
    def load_parser_config(self):
        pass
            
            
    # ---- CURRENCY TABS MANAGEMENT
    def create_currency_tabs(self):
        for pb in self.user_sf_data['pricebooks']:
            idx = self.currency_tab_next_id
            self.currency_tab_next_id += 1
            
            tab = CurrencyTab(idx, self.user_sf_data["available_currencies"])
            
            self.all_currency_tabs[f'{pb}'] = tab
            
    
    def update_currency_tabs(self):
        self.ui.currency_tabs.clear()
        for i in range(self.ui.pricebooks_list.count()):
            item = self.ui.pricebooks_list.item(i)
            if item.checkState() == Qt.Checked:
                pricebook_name = item.text()
                tab_to_load = self.all_currency_tabs[pricebook_name]
                self.ui.currency_tabs.addTab(tab_to_load, pricebook_name)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = ParserEditorWindow()
    window.show()

    sys.exit(app.exec())
