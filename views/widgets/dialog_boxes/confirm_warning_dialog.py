from PySide6.QtWidgets import QMessageBox

class ConfirmWarningDialog(QMessageBox):
    
    def __init__(self, title: str, text: str, parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning) 
        self.setWindowTitle(title) 
        self.setText(text)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No) 
        self.setDefaultButton(QMessageBox.No)
        

def confirm_warning_result(title: str, text: str) -> bool:
    result = ConfirmWarningDialog(title, text)
    return result.exec() == QMessageBox.Yes