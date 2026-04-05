from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtCore import Qt
from ui.ui_import_progress_bar import Ui_ImportProgressBar


class ProgressBarDialog(QDialog):
    
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        
        self.setModal(True)
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint
        )
        
        self.text = text if text else 'Proccessing...'
        
        self.ui = Ui_ImportProgressBar()
        self.ui.setupUi(self)
        
        self.ui.infoLabel.setText(self.text)
        
    def set_text(self, text: str):
        self.ui.infoLabel.setText(text)
        