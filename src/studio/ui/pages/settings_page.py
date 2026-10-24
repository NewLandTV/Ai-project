from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SettingsPage(QWidget):
    def __init__(self):
        """TODO: OBS 등 외부 방송과 프로그램 연결 설정 바로가기 등등"""
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("설정 화면"))