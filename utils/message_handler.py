from PySide6.QtWidgets import QMessageBox


class MessageHandler:
    
    @staticmethod
    def show_error(parent, title: str, message: str, details: Exception = None):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        if details:
            msg_box.setDetailedText(str(details))
        msg_box.exec()

    @staticmethod
    def show_warning(parent, title: str, message: str):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
        
    @staticmethod
    def show_info(parent, title: str, message: str):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()