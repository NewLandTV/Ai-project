import sys
from PySide6.QtWidgets import QApplication
from studio.ui.main_window import MainWindow

async def run(chatbot, obs):
    app = QApplication()

    window = MainWindow(chatbot)
    window.show()

    sys.exit(app.exec())