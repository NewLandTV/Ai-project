import commands

async def run(chatbot, obs):
    while True:
        word = input("메시지 입력 : ")
        if not commands.try_run(word):  # 채팅이 명령이 아닐 때만 AI가 답변하기
            text = ""
            for answer in chatbot.get_response(word):
                text += answer
                obs.update_obs_text("Answer Text", text)
                print(answer, end='', flush=True)
            print()