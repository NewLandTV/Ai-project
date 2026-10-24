from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QScrollArea
)
from PySide6.QtCore import Qt, Signal
from studio.core.controller import ChatController
from studio.ui.components.submit_text_edit import SubmitTextEdit
from studio.ui.components.message_bubble import MessageBubble
from studio.ui.components.typing_bubble import TypingBubble

class ChatPage(QWidget):
    send_to_worker = Signal(str)
    
    def __init__(self, chatbot):
        super().__init__()

        self.chatbot = chatbot  # 챗봇 (Ai)

        # 컨트롤러와 연결
        self.controller = ChatController(chatbot)
        self.controller.response_ready.connect(
            lambda text: self.add_message(text, False)
        )
        self.controller.error_occurred.connect(
            lambda message: self.add_message(f"AI 오류: {message}", False)
        )
        self.controller.typing_changed.connect(
            lambda visible: self.set_typing_visible(visible)
        )
        
        # Ai 답변 대기 관련 요소
        self.typing_bubble = TypingBubble()

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
        self.send_btn.setFixedHeight(70)

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
        self.controller.submit_message(text)

    def set_typing_visible(self, visible: bool):
        if visible:
            if self.messages_layout.indexOf(self.typing_bubble) == -1:
                self.messages_layout.addWidget(self.typing_bubble)
            self.typing_bubble.show()
        else:
            self.messages_layout.removeWidget(self.typing_bubble)
            self.typing_bubble.hide()

        scrollbar = self.scroll_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def on_ai_response(self, text):
        self.set_typing_visible(False)
        self.add_message(text, False)   # Ai 답변 표시