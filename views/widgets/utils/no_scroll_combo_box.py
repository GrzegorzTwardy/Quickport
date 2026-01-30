from PySide6.QtWidgets import QComboBox


class NoScrollComboBox(QComboBox):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
    def wheelEvent(self, event):
        if self.view().isVisible():
            super().wheelEvent(event) 
        else:
            event.ignore() 
