from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

class MessageBubble(QWidget):
    def __init__(self, text: str, is_user: bool):
        super().__init__()

        layout = QHBoxLayout(self)

        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(500)

        if is_user:
            self.label.setStyleSheet("""
                background-color: #2563eb;
                color: white;
                padding: 12px;
                border-radius: 16px;
            """)
            layout.addStretch()
            layout.addWidget(self.label)
        else:
            self.label.setStyleSheet("""
                background-color: #1f2937;
                color: white;
                padding: 12px;
                border-radius: 16px;
            """)
            layout.addWidget(self.label)
            layout.addStretch()