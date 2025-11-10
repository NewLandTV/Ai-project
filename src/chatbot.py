import ollama

class Chatbot:
    def __init__(self, model="mistral", messages=[{"role": "system", "content": "You are a helpful assistant."}]):
        self.model = model
        self.messages = messages

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