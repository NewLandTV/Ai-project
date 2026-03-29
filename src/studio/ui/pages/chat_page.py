from collections import deque
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QScrollArea
)
from PySide6.QtCore import Qt, QThread, Signal
from studio.core.ai_worker import AIWorker
from studio.ui.components.submit_text_edit import SubmitTextEdit
from studio.ui.components.message_bubble import MessageBubble
from studio.ui.components.typing_bubble import TypingBubble

class ChatPage(QWidget):
    send_to_worker = Signal(str)
    
    def __init__(self, chatbot):
        super().__init__()

        self.chatbot = chatbot  # 챗봇 (Ai)
        
        # Ai 답변과 대기 관련 변수
        self.typing_bubble = TypingBubble()
        self.queue = deque()
        self.processing = False

        # UI와 Ai 로직을 다른 스레드로 실행하기
        self.main_thread = QThread()
        self.worker = AIWorker(chatbot)
        self.worker.moveToThread(self.main_thread)

        self.main_thread.started.connect(lambda: None)
        self.worker.response_ready.connect(self.on_ai_response)
        self.send_to_worker.connect(self.worker.process)

        self.main_thread.start()

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
        self.queue.append(text) # 메시지 큐에 추가 (작업 대기열)
        self.process_next() # 대기 중이 아니면 메시지 큐 처리하기

    def process_next(self):
        if self.processing or len(self.queue) == 0:
            return
        self.processing = True

        text = self.queue.popleft()

        self.show_typing()
        self.send_to_worker.emit(text)  # Ai에게 메시지 보내고 화면에 응답 표시 (비동기 작업)

    def show_typing(self):
        self.messages_layout.addWidget(self.typing_bubble)

        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )

    def hide_typing(self):
        self.typing_bubble.setParent(None)

    def on_ai_response(self, text):
        self.processing = False

        self.hide_typing()
        self.add_message(text, False)   # Ai 답변 표시
        self.process_next() # 다음 메시지 큐 처리