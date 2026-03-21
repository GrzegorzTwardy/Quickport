from pathlib import Path
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from ui.dialog_boxes.ui_settings_dialog import Ui_SettingsDialog
from core.settings.settings_manager import settings_manager
from utils.message_handler import MessageHandler


class SettingsDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.last_saved_settings_snapshot = settings_manager.get_all_settings()
        
        self.ui.setupUi(self)
        self.load_settings()
        
        self.ui.maxRowsSpinBox.valueChanged.connect(lambda: self.validate_input('max_table_records'))
        self.ui.outputPathLineEdit.editingFinished.connect(lambda: self.validate_input('output_path'))
        self.ui.chooseFolderButton.clicked.connect(self.choose_folder)
        self.ui.resetButton.clicked.connect(self.reset_settings)
        self.ui.resetButton.clearFocus()
        self.ui.saveButton.clicked.connect(self.save_settings)
    
    
    def load_settings(self):
        self.ui.maxRowsSpinBox.setValue(settings_manager.get_setting('max_table_records'))
        self.ui.outputPathLineEdit.setText(settings_manager.get_setting('output_path'))
    
    
    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose folder', '')
        
        if folder_path:
            self.ui.outputPathLineEdit.setText(folder_path)
    
    
    def closeEvent(self, event):
        if self.ui.saveButton.isEnabled():
            if QMessageBox.question(self, 'Confimation', 'Do you want to exit without saving changes?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
    
    
    def has_changed(self) -> bool:
        return (
            Path(self.last_saved_settings_snapshot['output_path']) != Path(self.ui.outputPathLineEdit.text()) or
            self.last_saved_settings_snapshot['max_table_records'] != self.ui.maxRowsSpinBox.value()
        )
        
    def toggle_save_button(self):
        if self.has_changed():
            self.ui.saveButton.setEnabled(True)
            self.ui.saveButton.setFocus()
        else:
            self.ui.saveButton.setEnabled(False)
    
    
    def validate_input(self, setting_name: str):
        if not setting_name:
            return
        
        if setting_name == 'output_path':
            path = self.ui.outputPathLineEdit.text()
            if not Path(path).exists():
                self.ui.outputPathLineEdit.setText(settings_manager.get_setting('output_path'))
                self.ui.outputPathLineEdit.setFocus()
                self.ui.outputPathLineEdit.selectAll()
                MessageHandler.show_warning(self, 'Input Error', 'Please enter an existing path.')
        
        self.toggle_save_button()
            
        
    def save_settings(self):
        try:
            settings_manager.change_setting('output_path', self.ui.outputPathLineEdit.text())
            settings_manager.change_setting('max_table_records', self.ui.maxRowsSpinBox.value())
            self.last_saved_settings_snapshot = settings_manager.get_all_settings()
            self.ui.outputPathLineEdit.setText(self.last_saved_settings_snapshot['output_path'])
            self.toggle_save_button()
            # self.close()
        except Exception as e:
            MessageHandler.show_error(self, 'Saving Error', f"An error ocurred while trying to save settings:\n'{str(e)}'")
    
            
    def reset_settings(self):
        if QMessageBox.question(self, 'Confimation', 'Do you want to reset all settings to default values?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            settings_manager.reset_settings()
            self.load_settings()
        
    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    settings_window = SettingsDialog()
    settings_window.show()
    
    sys.exit(app.exec())