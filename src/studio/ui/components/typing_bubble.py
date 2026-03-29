from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import QTimer

class TypingBubble(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        
        self.text = "Ai가 답볍을 생각하고 있어요"
        self.label = QLabel(self.text)

        self.label.setStyleSheet("""
            background-color: #1f2937;
            color: white;
            padding: 12px;
            border-radius: 16px;
        """)
        layout.addWidget(self.label)
        layout.addStretch()
        
        # 점 애니메이션
        self.dots = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(500)

    def animate(self):
        self.dots = (self.dots + 1) % 4 # 점은 최소 1개, 최대 3개까지 반복
        self.label.setText(f"{self.text}{"." * self.dots}")