# tesing 
import sys
from PySide6.QtWidgets import QApplication
from views.main_menu_window import MainMenuWindow

app = QApplication(sys.argv)

main_menu = MainMenuWindow()
main_menu.show()

sys.exit(app.exec())