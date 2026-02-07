from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QPoint
from views.widgets.utils.field_metadata_popup import FieldMetadataPopup


class HoverComboBox(QComboBox):
    
    def __init__(self, metadata: dict | None, parent=None):
        super().__init__(parent)
        self.metadata = metadata if metadata else {}
        self.popup: FieldMetadataPopup | None = None

        self.setMouseTracking(True)

    def updateData(self, new_metadata: dict):
        self.metadata = new_metadata
        if self.popup:
            self.popup.deleteLater()
            self.popup = None

    def enterEvent(self, event):
        if not self.metadata:
            super().enterEvent(event)
            return

        if not self.popup:
            self.popup = FieldMetadataPopup(self.metadata)

        pos = self.mapToGlobal(self.rect().bottomRight())
        self.popup.move(pos + QPoint(6, 6))
        self.popup.show()

        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.popup:
            self.popup.hide()
        super().leaveEvent(event)

    def setToolTip(self, text):
        pass
    
    # no scroll
    def wheelEvent(self, event):
        if self.view().isVisible():
            super().wheelEvent(event) 
        else:
            event.ignore()