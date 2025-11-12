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
        response = ollama.chat(model=self.model, messages=self.messages)
        output = response.message.content
        self.messages.append({"role": "assistant", "content": output})
        return output
    
    def run(self):
        print("=== AI와 대화하기 ===")
        print("종료하려면 'exit' 또는 'quit'을 입력하세요.\n")
        
        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("챗봇을 종료합니다.")
                break

            answer = self.get_response(user_input)
            print(f"AI: {answer}")