from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QPoint
from views.widgets.utils.field_metadata_popup import FieldMetadataPopup


class HoverLabel(QLabel):

    def __init__(self, text: str, metadata: dict, parent=None):
        super().__init__(text, parent)
        self.metadata = metadata
        self.popup: FieldMetadataPopup | None = None

        self.setMouseTracking(True)

    def enterEvent(self, event):
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
