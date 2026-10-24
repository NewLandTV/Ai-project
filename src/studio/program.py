import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from studio.ui.main_window import MainWindow

def load_stylesheet(app: QApplication):
    """styles.qss를 스튜디오 프로그램 전체에 적용합니다."""
    stylesheet_path = Path(".").resolve() / "src" / "studio" / "assets" / "styles.qss"
    print(f"{stylesheet_path}에서 스타일을 불러오는 중입니다...")

    try:
        stylesheet = stylesheet_path.read_text(encoding="utf-8")
        app.setStyleSheet(stylesheet)
        print("스타일을 성공적으로 불러왔습니다.")
    except OSError as e:
        print("styles.qss 파일을 불러오지 못했습니다:", e)

async def run(chatbot, obs):
    app = QApplication()

    # 전역 스타일 적용
    load_stylesheet(app)

    # 프로그램 창 만들기
    window = MainWindow(chatbot)
    window.show()

    # 앱 실행
    sys.exit(app.exec())