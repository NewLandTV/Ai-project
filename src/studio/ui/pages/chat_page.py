from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
from studio.ui.components.submit_text_edit import SubmitTextEdit
from studio.ui.components.message_bubble import MessageBubble

class ChatPage(QWidget):
    def __init__(self, chatbot):
        super().__init__()

        self.chatbot = chatbot  # 챗봇 (Ai)

        # 전체 레이아웃
        main_layout = QVBoxLayout(self)

        # 스크롤 영역
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.container = QWidget()
        self.messages_layout = QVBoxLayout(self.container)
        self.messages_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.container)

        # 입력 영역
        input_layout = QHBoxLayout()

        self.input_box = SubmitTextEdit(self.send_message)
        self.input_box.setFixedHeight(70)
        
        self.send_btn = QPushButton("보내기")

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_btn)

        # 레이아웃 결합
        main_layout.addWidget(self.scroll_area)
        main_layout.addLayout(input_layout)

        # 이벤트 연결
        self.send_btn.clicked.connect(self.send_message)

    def add_message(self, text: str, is_user: bool):
        bubble = MessageBubble(text, is_user)

        self.messages_layout.addWidget(bubble)

        # 자동 스크롤
        scrollbar = self.scroll_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def send_message(self):
        text = self.input_box.toPlainText().strip()
        if not text:
            return
        
        # 사용자 메시지 처리
        self.add_message(text, True)
        self.input_box.clear()

        # Ai에게 메시지 보내고 화면에 응답 표시
        response = ""
        for chunk in self.chatbot.get_response(text):
            response += chunk

        self.add_message(response, False)