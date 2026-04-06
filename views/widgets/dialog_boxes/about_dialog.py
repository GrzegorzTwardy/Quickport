from PySide6.QtWidgets import QDialog
from ui.dialog_boxes.ui_about_dialog import Ui_AboutDialog

class AboutDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.close)
        
        self.ui.version_value_label.setText('v1.0.1-alpha')
        self.ui.info_value_label.setOpenExternalLinks(True)
        
        
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    dialog = AboutDialog()
    dialog.show()
    
    sys.exit(app.exec())