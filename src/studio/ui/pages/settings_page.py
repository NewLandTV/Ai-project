from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("설정 화면"))