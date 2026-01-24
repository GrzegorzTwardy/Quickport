from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class FieldMetadataPopup(QFrame):

    def __init__(self, metadata: dict, parent=None):
        super().__init__(parent, Qt.ToolTip)

        self.setWindowFlags(
            Qt.ToolTip | Qt.FramelessWindowHint
        )
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)

        for key, value in metadata.items():
            label = QLabel(f"<b>{key}</b>: {value}")
            label.setTextFormat(Qt.RichText)
            layout.addWidget(label)

        self.setStyleSheet("""
            QFrame {
                background: #2b2b2b;
                color: white;
                border-radius: 4px;
            }
        """)
