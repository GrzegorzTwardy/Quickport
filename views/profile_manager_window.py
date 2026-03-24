from PySide6.QtWidgets import (
    QWidget, QMessageBox, QListWidgetItem, QDialog
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, Qt
from core.profile.profile_model import Profile
from ui.ui_profile_manager import Ui_ProfileManager
from core.profile.profile_service import ProfileService
from dtos.sf_metadata import SfMetadata
from dtos.credentials import Credentials
from salesforce_api.authenticator import Authenticator
from salesforce_api.salesforce_api import SalesforceApi
from exceptions.login_exceptions import *
from utils.message_handler import MessageHandler
from views.widgets.profile_config import ProfileConfigDialog


# TODO: change focus when new profile is added or edited
  
class ProfileManagerWindow(QWidget):
    
    def __init__(self, session):
        super().__init__()
        
        self.session = session
        self.sf_api = None
        self.full_name = None
        self.env_name = None

        self.profile_service = ProfileService()
        
        self.ui = Ui_ProfileManager()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon())
        
        self._connect_signals()
        self.load_profiles()
    
    
    def _connect_signals(self):
        self.ui.addProfileButton.clicked.connect(self.add_new_profile)
        self.ui.editProfileButton.clicked.connect(self.edit_profile)
        self.ui.deteleProfileButton.clicked.connect(self.delete_selected_profile)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.profileList.currentItemChanged.connect(self.change_description)
    
    
    def get_selected_profile(self) -> Profile:
        item = self.ui.profileList.currentItem()

        if item is not None:
            return item.data(Qt.UserRole)
        else:
            return None
    
    
    def toggle_buttons(self):
        not_empty = self.ui.profileList.count() > 0
        self.ui.editProfileButton.setEnabled(not_empty)
        self.ui.deteleProfileButton.setEnabled(not_empty)
        self.ui.loginButton.setEnabled(not_empty)
        self.ui.logToSandbox.setEnabled(not_empty)
       
        
    def change_description(self):
        profile = self.get_selected_profile()

        if profile is not None:
            self.ui.descTextEdit.setText(profile.desc)
        else:
            self.ui.descTextEdit.clear()
    
    
    def load_profiles(self):
        self.ui.profileList.clear()
        
        self.profile_service.get_all_profiles()
        
        for profile in self.profile_service.profiles:
            item = QListWidgetItem(profile.name)
            item.setData(Qt.UserRole, profile)
            self.ui.profileList.addItem(item)
        
        if self.ui.profileList.count():
            self.ui.profileList.setCurrentRow(0)
            self.toggle_buttons()
            
    
    # ============== PROFILE MANAGEMENT ================  
    def add_new_profile(self):
        add_profile_dialog = ProfileConfigDialog(None)
        
        if add_profile_dialog.exec() == QDialog.Accepted:
            profile_data = add_profile_dialog.get_data()
            self.profile_service.add_new_profile(
                name=profile_data['name'],
                production_client_id=profile_data['prod_client_id'],
                sandbox_client_id='sandbox_client_id',
                desc=profile_data['desc']
            )
            self.load_profiles()
            self.toggle_buttons()

        
    def edit_profile(self):
        profile = self.get_selected_profile()
        
        edit_profile_dialog = ProfileConfigDialog(profile)
        
        if edit_profile_dialog.exec() == QDialog.Accepted:
            profile_data = edit_profile_dialog.get_data()
            self.profile_service.edit_profile(
                target_profile_name=profile.name,
                name=profile_data['name'],
                production_client_id=profile_data['prod_client_id'],
                sandbox_client_id=profile_data['sandbox_client_id'],
                desc=profile_data['desc']
            )
            self.load_profiles()
        
    
    def confirm_operation(self, operation, obj):
        title = 'Confirming Operation'
        msg = 'Do you want to confirm this operation?'
        default_option = QMessageBox.Yes
        
        match operation:
            case 'delete':
                title = 'Deleting Profile'
                msg = f"Are you sure you want to delete '{obj}' profile?"
                default_option = QMessageBox.No
            case 'edit':
                title = 'Exit Profile Editing'
                msg = 'Do you want to exit without saving changes?'
                default_option = QMessageBox.No
        
        reply = QMessageBox.question(
            self,
            title,
            msg,
            QMessageBox.Yes | QMessageBox.No,
            default_option
        )
        return reply == QMessageBox.Yes
    
    
    def delete_selected_profile(self):
        item = self.ui.profileList.currentItem()

        if item is not None:
            profile = item.data(Qt.UserRole)

            if self.confirm_operation('delete', profile.name):
                self.profile_service.remove_profile(profile.name)

                row = self.ui.profileList.row(item)
                self.ui.profileList.takeItem(row)
            
                self.toggle_buttons()
                self.load_profiles()
    # ===========================================
    
    
    # ============== LOGIN LOGIC ================ 
    def handle_login_success(self, token_response):

        def validate_metadata(sf_metadata: SfMetadata):
            errors_msgs = []

            if len(sf_metadata.available_currencies) == 0:
                errors_msgs.append('avaliable currencies')
            if len(sf_metadata.pricebooks) == 0:
                errors_msgs.append('pricebooks')
            if len(sf_metadata.product2_fields) == 0:
                errors_msgs.append('Product2 fields')
            elif 'ProductCode' not in sf_metadata.product2_fields:
                errors_msgs.append("'ProductCode' field in Product2 object (obligatory field)")
                
            if errors_msgs:
                msg = 'This profile does not contain/is missing data required for the application to function:\n'
                for m in errors_msgs:
                    msg += f"- {m}\n"
                
                raise InvalidSfMetadataError(msg.rstrip())

        try:
            self.full_name = Authenticator.get_user_display_name(
                identity_url=token_response['id'], 
                access_token=token_response['access_token']
            )

            creds = Credentials(
                access_token=token_response['access_token'],
                refresh_token=token_response.get('refresh_token'),
                instance_url=token_response['instance_url'],
                client_id=self.auth_thread.client_id
            )

            self.sf_api = SalesforceApi(creds=creds)

            sf_metadata = self.sf_api.get_user_sf_metadata()
            
            # validate user's Salesforce info
            validate_metadata(sf_metadata)

            # --- get env name to dipsplay it in main menu
            item = self.ui.profileList.currentItem()

            if item is not None:
                self.env_name = item.text()
            # ---

            self.session.login(sf_metadata)
            
            self.ui.loginButton.setText("Log In")
            self.ui.loginButton.setEnabled(True)
            
            MessageHandler.show_info(self, "Success", f"Successfully logged as:\n{self.full_name}")
        
        # Data Validation / API errors (after successfull login)
        except Exception as e:
            self.ui.loginButton.setText('Log In')
            self.ui.loginButton.setEnabled(True)
            MessageHandler.show_error(self, 'Post-Login Error', 'An error occurred while fetching metadata:', str(e))


    # Authorization Errors
    def handle_login_error(self, error_msg):
        self.ui.loginButton.setText("Login")
        self.ui.loginButton.setEnabled(True)
        
        if "has been canceled" not in error_msg.lower():
            MessageHandler.show_error(self, 'Login Error', 'An error occurred while trying to log in:', error_msg)
        
        
    def login(self):
        try:
            if hasattr(self, 'auth_thread') and self.auth_thread.isRunning():
                self.auth_thread.cancel()
                self.ui.loginButton.setEnabled(False)
                self.ui.loginButton.setText("Cancelling...")
                return
            
            client_id = None
            login_url = None
            profile = None
            profile_item = self.ui.profileList.currentItem()
            
            if profile_item is not None:      
                profile = profile_item.data(Qt.UserRole)
            else:
                raise ValueError('No profile selected')
            
            if self.ui.logToSandbox.isChecked():
                login_url = "https://test.salesforce.com"
                client_id = profile.sandbox_client_id
            else:
                login_url = "https://login.salesforce.com"
                client_id = profile.production_client_id
            
            if not client_id:
                raise ClientIdNotFoundError()
            
            self.ui.loginButton.setEnabled(True)
            self.ui.loginButton.setText("Cancel")

            # using "self." so it doesn't end up in the garbage collector
            self.auth_thread = Authenticator(
                client_id=client_id,
                login_url=login_url
            )

            self.auth_thread.login_successful.connect(self.handle_login_success)
            self.auth_thread.login_failed.connect(self.handle_login_error)

            self.auth_thread.start()
            
        except ClientIdNotFoundError as e:
            self.ui.loginButton.setEnabled(True)
            self.ui.loginButton.setText("Login")
            org_type = 'sandbox' if self.ui.logToSandbox.isChecked() else 'production'
            MessageHandler.show_warning(self, 'Client ID Error', f'Selected profile is missing {org_type} client ID.')
            
        except Exception as e:
            self.ui.loginButton.setEnabled(True)
            self.ui.loginButton.setText("Login")
            if "has been canceled" not in str(e):
                MessageHandler.show_error(self, 'Login Error', 'An error occured while trying to log in.', str(e))
    # ====================================================
    
    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    from dtos.session import AppSession
    
    app = QApplication(sys.argv)
    
    profile_manager_window = ProfileManagerWindow(AppSession())
    profile_manager_window.show()
    
    sys.exit(app.exec())