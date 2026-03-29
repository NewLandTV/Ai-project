import asyncio
from PySide6.QtCore import QObject, Signal, Slot

class AIWorker(QObject):
    response_ready = Signal(str)

    def __init__(self, chatbot):
        super().__init__()

        self.chatbot = chatbot

    @Slot(str)
    def process(self, text):
        asyncio.run(self.run_ai(text))

    async def run_ai(self, text):
        response = "".join(self.chatbot.get_response(text))
        self.response_ready.emit(response)