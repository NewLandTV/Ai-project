import os
from .setup import *
import websockets

if os.path.exists(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), "customfunc.py")))):
    from .customfunc import *

async def run(chatbot):
    try:
        websocket = await websockets.connect("ws://127.0.0.1:8001")
    except Exception as e:
        print("Couldn't connect to vtube studio:", e)
        input("press enter to quit program")
        quit()
    command_list = await setup(websocket)
    while True:
        is_command = False
        word = input("enter command ")
        for key in command_list["COMMANDS"]:
            if word == key:
                print("executing")
                mdinf = await getmd(websocket)
                s = mdinf["data"]["modelPosition"]["size"]
                r = mdinf["data"]["modelPosition"]["rotation"]
                x = mdinf["data"]["modelPosition"]["positionX"]
                y = mdinf["data"]["modelPosition"]["positionY"]
                cm = command_list["COMMANDS"][key]
                await eval(cm)
                is_command = True
                break
        if not is_command:  # 채팅이 명령이 아닐 때만 AI가 답변하기
            answer = chatbot.get_response(word)
            with open("answer.txt", "w", encoding="utf-8") as f:
                f.write(f"{answer}")
            print(answer)