import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from views.main_menu_window import MainMenuWindow
from core.settings.settings_manager import settings_manager
from exceptions.global_exceptions import *
from utils.message_handler import MessageHandler

def main() -> None:
    app = QApplication(sys.argv)
    
    try:
        settings_manager.load_settings() 
        
        # === icon management ===
        if os.name == 'nt':
            import ctypes
            myappid = 'quickport.app' 
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path = settings_manager.get_setting('icon_path')
        app.setWindowIcon(QIcon(icon_path))
        # ====================== 

        main_menu = MainMenuWindow()
        main_menu.show()

        sys.exit(app.exec())
    except SettingsError as e:
        MessageHandler.show_error(None, 'Critical Error', str(e))
        sys.exit(1)
            

if __name__ == '__main__':
    main()