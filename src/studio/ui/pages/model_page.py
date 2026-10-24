from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ModelPage(QWidget):
    def __init__(self):
        """TODO: Ai 모델 설정 페이지, json 저장, 개인 프로필 맞춤 설정 등등"""
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("모델 설정"))