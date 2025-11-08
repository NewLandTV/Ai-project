import ollama

def get_ai_response(user_input):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                
                "role": "user",
                "content": user_input
            }
        ],
    )
    return response.message.content

def run():
    print("=== AI와 대화하기 ===")
    print("종료하려면 'exit' 또는 'quit'을 입력하세요.\n")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("챗봇을 종료합니다.")
            break

        answer = get_ai_response(user_input)
        print(f"AI: {answer}")