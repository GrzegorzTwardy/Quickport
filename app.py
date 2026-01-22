# tesing 
import sys
from PySide6.QtWidgets import QApplication
from dtos.session import AppSession
from core.profile.profile_model import Profile
from views.mapper_editor_window import MapperEditorWindow
from salesforce_api.salesforce_api import SalesforceApi

profile = Profile.from_json('./cert/test_creds.json')    
sf_api = SalesforceApi(profile)
sf_api.connect()

session = AppSession()
session.login(
    user_id='123213', 
    sf_metadata=sf_api.get_user_sf_metadata()
)

app = QApplication(sys.argv)

window = MapperEditorWindow(session, None)
window.show()

sys.exit(app.exec())