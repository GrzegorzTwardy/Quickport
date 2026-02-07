from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QPoint
from views.widgets.utils.field_metadata_popup import FieldMetadataPopup


class HoverLabel(QLabel):

    def __init__(self, text: str, metadata: dict, parent=None):
        super().__init__(text, parent)
        self.metadata = metadata
        self.popup: FieldMetadataPopup | None = None

        self._locked_open = False

        self.setMouseTracking(True)

    def show_popup_manual(self):
        if not self.metadata:
            return
        self._create_popup_if_needed()
        self._locked_open = True
        self.popup.show()

    def hide_popup_manual(self):
        self._locked_open = False
        if self.popup:
            self.popup.hide()

    def _create_popup_if_needed(self):
        if not self.popup:
            self.popup = FieldMetadataPopup(self.metadata)
        pos = self.mapToGlobal(self.rect().bottomRight())
        self.popup.move(pos + QPoint(6, 6))

    def enterEvent(self, event):
        if self.metadata:
            self._create_popup_if_needed()
            self.popup.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self._locked_open:
            return
        if self.popup:
            self.popup.hide()
        super().leaveEvent(event)
