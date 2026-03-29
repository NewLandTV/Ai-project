from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

class SubmitTextEdit(QTextEdit):
    def __init__(self, submit_method):
        super().__init__()

        self.submit_method = submit_method

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return and not event.modifiers():
            self.submit_method()
            return

        return super().keyPressEvent(event)