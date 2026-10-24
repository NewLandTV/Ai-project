from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

class MessageBubble(QWidget):
    def __init__(self, text: str, is_user: bool):
        super().__init__()

        layout = QHBoxLayout(self)

        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(500)

        # 메시지 종류에 따라 스타일 설정하기
        message_type = "user" if is_user else "ai"
        self.label.setProperty("messageType", message_type)

        # 레이아웃 정렬
        if is_user:
            layout.addStretch()
            layout.addWidget(self.label)
        else:
            layout.addWidget(self.label)
            layout.addStretch()