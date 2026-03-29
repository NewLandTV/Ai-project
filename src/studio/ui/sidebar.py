from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.btn_chat = QPushButton("채팅")
        self.btn_model = QPushButton("모델")
        self.btn_settings = QPushButton("설정")

        layout.addWidget(self.btn_chat)
        layout.addWidget(self.btn_model)
        layout.addWidget(self.btn_settings)
        
        layout.addStretch()