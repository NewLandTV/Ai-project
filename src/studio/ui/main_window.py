from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QStackedWidget
)
from ..ui.sidebar import Sidebar
from ..ui.topbar import TopBar
from ..ui.pages.chat_page import ChatPage
from ..ui.pages.model_page import ModelPage
from ..ui.pages.settings_page import SettingsPage

class MainWindow(QMainWindow):
    def __init__(self, chatbot):
        super().__init__()
        self.setWindowTitle("Ai 스튜디오")
        self.resize(1280, 720)

        # 중앙 위젯 설정
        central = QWidget()
        self.setCentralWidget(central)

        # 전체 레이아웃
        main_layout = QHBoxLayout(central)

        # 사이드바
        self.sidebar = Sidebar()

        # 내용
        content_layout = QVBoxLayout()

        self.topbar = TopBar(chatbot)

        # 페이지
        self.stack = QStackedWidget()
        self.chat_page = ChatPage(chatbot)
        self.model_page = ModelPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.chat_page)
        self.stack.addWidget(self.model_page)
        self.stack.addWidget(self.settings_page)

        content_layout.addWidget(self.topbar)
        content_layout.addWidget(self.stack)

        # 레이아웃 결합
        main_layout.addWidget(self.sidebar, 1)
        main_layout.addLayout(content_layout, 4)

        # 이벤트 연결
        self.sidebar.btn_chat.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.sidebar.btn_model.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.sidebar.btn_settings.clicked.connect(lambda: self.stack.setCurrentIndex(2))