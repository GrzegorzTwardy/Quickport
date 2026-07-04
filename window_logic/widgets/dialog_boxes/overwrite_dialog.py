from PySide6.QtWidgets import QApplication, QMessageBox

class OverwriteDialog(QMessageBox):
    
    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning) 
        self.setWindowTitle('Overwrite Confirmation') 
        self.setText(f'"{path}" already exists.\nDo you want to overwrite it?') 
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No) 
        self.setDefaultButton(QMessageBox.No)
        
        
def overwrite_dialog_result(path) -> bool:
    dialog = OverwriteDialog(path)
    return dialog.exec() == QMessageBox.Yes


if __name__ == "__main__":
    app = QApplication([])
    
    if overwrite_dialog_result('dat3243243254343ffr4a.txt'): 
        print('confirmed') 
    else: print('denied') 
