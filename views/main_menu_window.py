from dtos.session import AppSession
from PySide6.QtWidgets import QMainWindow
from ui.ui_main_menu import Ui_MainMenu

from views.mapper_list_window import MapperListWindow


class MainMenuWindow(QMainWindow):
    
    def __init__(self, session: AppSession | None):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        
        self.session = session
        
        # views
        self.mapper_list_window = None
        
        # connecting signals
        self.session.user_logged_in.connect(self.on_login)
        self.session.user_logged_out.connect(self.on_logout)
        self.ui.mappersButton.clicked.connect(self.open_mapper_list)
        
        
    def on_login(self):
        self.ui.exportPricebookGroupBox.setEnabled(True)
        self.ui.mappersButton.setEnabled(True)
        if self.session.user_id:
            self.ui.currentUsernameLabel.setText(self.session.user_id)

    
    def on_logout(self):
        self.ui.exportPricebookGroupBox.setEnabled(False)
        self.ui.mappersButton.setEnabled(False)
        
        
    def open_mapper_list(self):
        if self.mapper_list_window is None:
            self.mapper_list_window = MapperListWindow(session)
            self.mapper_list_window.destroyed.connect(lambda: setattr(self, 'mapper_list_window', None))
            self.mapper_list_window.show()
        else:
            self.mapper_list_window.show()
            self.mapper_list_window.activateWindow()
        
        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    # from PySide6.QtCore import QTimer
    from core.profile.profile_model import Profile
    from salesforce_api.salesforce_api import SalesforceApi

    profile = Profile.from_json('./cert/test_creds.json')    
    sf_api = SalesforceApi(profile)
    sf_api.connect()

    app = QApplication(sys.argv)
    session = AppSession()

    window = MainMenuWindow(session)
    window.show()
    
    # session.test_login()
    session.login(
        user_id='123213', 
        sf_metadata=sf_api.get_user_sf_metadata()
    )
    
    # QTimer.singleShot(5000, lambda: session.logout())
    sys.exit(app.exec())