from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
from ui.ui_profile_config import Ui_ProfileConfig
from core.profile.profile_service import ProfileService
from core.profile.profile_model import Profile
from utils.message_handler import MessageHandler


class ProfileConfigDialog(QDialog):
    
    def __init__(self, profile_to_edit: Profile | None, parent=None):
        super().__init__(parent)
        
        self.profile_data = {}
        self.profile_to_edit = profile_to_edit
        
        profile_service = ProfileService()
        self.used_names = [profile.name for profile in profile_service.get_all_profiles()]
        
        self.ui = Ui_ProfileConfig()
        self.ui.setupUi(self)
            
        self.ui.buttonBox.accepted.disconnect() 
        self.ui.buttonBox.accepted.connect(self.on_accept)
        
        if profile_to_edit:
            self.update_inputs()
        

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
            'desc': desc
        }
        
        return True
    
    
    def get_data(self):  
        return self.profile_data
        
        
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    prof_service = ProfileService()
    profile = prof_service.get_profile_by_name('Do usunięcia')
    
    profile_config_dialog = ProfileConfigDialog(profile)
    
    if profile_config_dialog.exec() == QDialog.Accepted:
        print(profile_config_dialog.get_data())
