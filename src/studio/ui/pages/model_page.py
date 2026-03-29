from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ModelPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("모델 설정"))