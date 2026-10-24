from collections import deque
from PySide6.QtCore import (
    QObject, QThread, Signal, Slot
)
from studio.core.ai_worker import AIWorker

class ChatController(QObject):
    send_to_worker = Signal(str)

    # 상태 및 결과를 UI로 전달
    response_ready = Signal(str)
    error_occurred = Signal(str)
    typing_changed = Signal(bool)

    def __init__(self, engine):
        super().__init__()

        self.queue = deque()
        self.processing = False

        self.thread = QThread(self)
        self.worker = AIWorker(engine)
        self.worker.moveToThread(self.thread)

        # 요청 전달
        self.send_to_worker.connect(self.worker.process)

        # 작업 결과 수신
        self.worker.response_ready.connect(self._on_response)
        self.worker.error_occurred.connect(self._on_error)

        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.start()

    def submit_message(self, text: str):
        """메시지를 대기열에 추가합니다."""
        self.queue.append(text)
        self._process_next()

    def _process_next(self):
        if self.processing or not self.queue:
            return

        self.processing = True
        text = self.queue.popleft()

        self.typing_changed.emit(True)
        self.send_to_worker.emit(text)

    @Slot(str)
    def _on_response(self, text: str):
        self.response_ready.emit(text)
        self._finish_request()

    @Slot(str)
    def _on_error(self, message: str):
        self.error_occurred.emit(message)
        self._finish_request()

    def _finish_request(self):
        self.processing = False
        self.typing_changed.emit(False)
        self._process_next()

    def shutdown(self):
        """앱 종료와 함께 작업 스레드를 종료합니다."""
        self.thread.quit()
        self.thread.wait()