from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QListWidget, QListWidgetItem, QWidget, QDialogButtonBox)
from ui.dialog_boxes.checkbox_list_dialog import Ui_CheckBoxListDialog

# requires at least 1 list item selected in oreder to process
class ChecklistDialog(QDialog):
    
    def __init__(self, available_items: list, user_operation: str, parent: QWidget | None):
        super().__init__(parent)
        self.ui = Ui_CheckBoxListDialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle(user_operation)

        if not available_items or len(available_items) == 0:
            raise ValueError('no currencies detected')
        
        self.ui.listWidget.setSelectionMode(QListWidget.NoSelection)
        
        for row in sorted(available_items):
            item = QListWidgetItem(row)
            item.setFlags(
                item.flags() 
                | Qt.ItemIsEnabled
            )
            
            item.setCheckState(Qt.Unchecked)
            self.ui.listWidget.addItem(item)

        self.ui.listWidget.itemPressed.connect(self.toggle_check)
        
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.listWidget.itemChanged.connect(self.update_ok_button)

    
    def update_ok_button(self):
        has_checked = any(
            self.ui.listWidget.item(i).checkState() == Qt.Checked
            for i in range(self.ui.listWidget.count())
        )
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(has_checked)

        
    def toggle_check(self, item): 
        if item.checkState() == Qt.Checked: 
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        
        
    def get_selected_items(self):
        checked_items = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if item.checkState() == Qt.Checked:
                checked_items.append(item.text())

        return checked_items

    

def execute_checklist_dialog(items: list, user_operation: str, parent: QWidget | None):
    dialog = ChecklistDialog(items, user_operation, parent=parent)
    result = dialog.exec() 
    
    if result == QDialog.Accepted: 
        return dialog.get_selected_items()
    else: 
        return None
    
    
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    
    result = execute_checklist_dialog(['EUR', 'PLN', 'CZK', 'USD'], 'Choose currency', None)
    
    if result:
        print(result)