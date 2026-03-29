from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

class TopBar(QWidget):
    def __init__(self, chatbot):
        super().__init__()

        layout = QHBoxLayout(self)

        self.label = QLabel(f"현재 모델: {chatbot.model}")
        
        layout.addWidget(self.label)
        layout.addStretch()