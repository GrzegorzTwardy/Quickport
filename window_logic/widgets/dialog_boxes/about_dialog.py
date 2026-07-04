import os
import sys
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from ui.dialog_boxes.ui_about_dialog import Ui_AboutDialog


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class AboutDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        
        real_image_path = get_resource_path('img/quickport-dark-logo.png')
        self.ui.image_label.setPixmap(QPixmap(real_image_path))
        
        self.ui.pushButton.clicked.connect(self.close)
        
        self.ui.version_value_label.setText('v1.0.1-beta')
        self.ui.info_value_label.setOpenExternalLinks(True)
        
        
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    dialog = AboutDialog()
    dialog.show()
    
    sys.exit(app.exec())