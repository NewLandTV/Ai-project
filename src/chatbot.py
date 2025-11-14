import ollama
from prompt import get_prompt_info

class Chatbot:
    def __init__(self, model="mistral"):
        self.model = model
        self.messages = []
        prompt = get_prompt_info()
        if prompt != None:  # prompt.txt가 존재하면 프롬프트 설정하기.
            self.messages.append({"role": "system", "content": prompt})

    def get_response(self, message):
        self.messages.append({"role": "user", "content": message})
        response = ""
        for chunk in ollama.chat(model=self.model, messages=self.messages, stream=True):
            text = chunk.message.content
            yield text
            response += text
        self.messages.append({"role": "assistant", "content": response})
        return response