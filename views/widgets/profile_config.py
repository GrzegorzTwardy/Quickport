from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui.ui_profile_config import Ui_ProfileConfig
from core.profile.profile_service import ProfileService
from core.profile.profile_model import Profile
from utils.message_handler import MessageHandler
from views.widgets.dialog_boxes.checklist_dialog import execute_checklist_dialog, ChecklistDialog
from utils.message_handler import MessageHandler


class ProfileConfigDialog(QDialog):
    
    def __init__(self, profile_to_edit: Profile | None, prod2_fields: list, parent=None):
        super().__init__(parent)
        
        self.prod2_fields = prod2_fields
        self.selected_fields = []
        
        self.profile_data = {}
        self.profile_to_edit = profile_to_edit
        
        profile_service = ProfileService()
        self.used_names = [profile.name for profile in profile_service.get_all_profiles()]
        
        self.ui = Ui_ProfileConfig()
        self.ui.setupUi(self)
            
        self.ui.buttonBox.accepted.disconnect() 
        self.ui.buttonBox.accepted.connect(self.on_accept)
        self.ui.manageFieldsButton.clicked.connect(self.open_checklist)
        self.ui.nameLe.setFocus()
        
        if profile_to_edit:
            # if edited profile != logged in profile => remove prod2 fields section
            if not self.prod2_fields:
                self.delete_prod2_fields_section()
                
            # update selected_fields
            for field in profile_to_edit.primary_key:
                if field in self.prod2_fields:
                    self.selected_fields.append(field)
                    
            if 'ProductCode' in self.prod2_fields and not self.selected_fields:
                self.selected_fields.append('ProductCode')
                    
            self.update_fields_label()
            self.update_inputs()
        else:
            # if adding new profile, we dont need to manage prod2 fields (first we have to log in)
            self.delete_prod2_fields_section()
        
        try:
            self.checklist_dialog = FieldsChecklistDialog(
                self.prod2_fields, 
                'Choose Product2 Fields',
                self.selected_fields,
                self
            ) if self.prod2_fields else None
        except ValueError as e:
            MessageHandler.show_error(self, 'Profile Error', 'The Salesforce environment associated to this account may be missing crucial informations:\nProduct2 object\'s fields.')
    
    
    def delete_widget(self, widget, layout):
        if widget:
            layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()
            
            
    def delete_prod2_fields_section(self):
        self.delete_widget(self.ui.manageFieldsButton, self.ui.gridLayout_3)
        self.delete_widget(self.ui.primaryKeyLabel, self.ui.gridLayout_3)
        self.delete_widget(self.ui.fieldListLabel, self.ui.gridLayout_3)

    
    def update_fields_label(self):
        self.ui.fieldListLabel.setText(',\n'.join(self.selected_fields))
    
    
    def open_checklist(self):
        if self.checklist_dialog.exec() == QDialog.Accepted: 
            self.selected_fields = self.checklist_dialog.get_selected_items()
            self.update_fields_label()
        else: 
            return None
    

    def update_inputs(self):
        self.ui.nameLe.setText(self.profile_to_edit.name)
        self.ui.prodCidLe.setText(self.profile_to_edit.production_client_id)
        
        if self.profile_to_edit.production_client_id:
            self.ui.prodCidCheckBox.setChecked(True)
            self.ui.prodCidLe.setText(self.profile_to_edit.production_client_id)
        else:
            self.ui.prodCidCheckBox.setChecked(False)
            
        if self.profile_to_edit.sandbox_client_id:
            self.ui.sandboxCidCheckBox.setChecked(True)
            self.ui.sandboxCidLe.setText(self.profile_to_edit.sandbox_client_id)
        else:
            self.ui.sandboxCidCheckBox.setChecked(False)
            
        self.ui.descTe.setPlainText(self.profile_to_edit.desc)
    
    
    def on_accept(self):
        if self.validate_inputs():
            self.accept()
            
        
    def validate_inputs(self) -> bool:
        name = self.ui.nameLe.text().strip()
        prod_client_id = self.ui.prodCidLe.text()
        sandbox_client_id = self.ui.sandboxCidLe.text()
        desc = self.ui.descTe.toPlainText()
        
        if name in self.used_names and self.profile_to_edit is None:
            MessageHandler.show_warning(self, 'Input Validation', f"A profile named '{name}' already exists.\nPlease choose another name.")
            return False
        
        # in edit mode: if name is changed, but it already exists
        if self.profile_to_edit and name != self.profile_to_edit.name and name in self.used_names:
             MessageHandler.show_warning(self, 'Input Validation', f"A profile named '{name}' already exists.")
             return False    
    
        if not name:
            MessageHandler.show_warning(self, 'Input Validation', 'Name cannot be empty.')
            return False
        if self.ui.prodCidCheckBox.isChecked() and not prod_client_id:
            MessageHandler.show_warning(self, 'Input Validation', 'Production Client ID has been set as required, please complete the input.')
            return False
        if self.ui.sandboxCidCheckBox.isChecked() and not sandbox_client_id:
            MessageHandler.show_warning(self, 'Input Validation', 'Sandbox Client ID has been set as required, please complete the input.')
            return False
        
        # if both checkboxes are unchecked -> error, at least one has to be checked
        if not self.ui.prodCidCheckBox.isChecked() and not self.ui.sandboxCidCheckBox.isChecked():
            MessageHandler.show_warning(self, 'Input Validation', 'You must provide at least 1 Client ID.')
            return False
        
        self.profile_data = {
            'name': name,
            'prod_client_id': prod_client_id,
            'sandbox_client_id': sandbox_client_id,
            'desc': desc,
            'primary_key': self.selected_fields
        }
        
        return True
    
    
    def get_data(self):  
        return self.profile_data
        

class FieldsChecklistDialog(ChecklistDialog):
    
    def __init__(self, available_items, user_operation, initial_set: list | None, parent):
        super().__init__(available_items, user_operation, parent)
        self.selected_rows = initial_set if initial_set else []
        self.update()
        
    def update(self):
        if self.selected_rows:
            for i in range(self.ui.listWidget.count()):
                item = self.ui.listWidget.item(i)
                if item.text() in self.selected_rows:
                    item.setCheckState(Qt.Checked)
                else:
                    item.setCheckState(Qt.Unchecked)
    
    def get_selected_items(self):
        checked_items = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if item.checkState() == Qt.Checked:
                checked_items.append(item.text())
        self.selected_rows = checked_items
        self.update()
        return checked_items
    

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    fields = ['ProductCode', 'Name', 'Price', 'Delivery']
    
    profile_config_dialog = ProfileConfigDialog(None, fields)
    
    if profile_config_dialog.exec() == QDialog.Accepted:
        print(profile_config_dialog.get_data())
