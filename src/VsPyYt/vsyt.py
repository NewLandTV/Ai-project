import os
import pytchat
from pytchat import *
from .setup import *
import websockets

if os.path.exists(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), "customfunc.py")))):
    from .customfunc import *

async def run(chatbot):
    try:
        websocket = await websockets.connect("ws://127.0.0.1:8001")
    except Exception as e:
        print("Couldn't connect to vtube studio", e)
        input("press enter to quit program")
        quit()
    command_list = await setup(websocket)
    # Main loops for youtube
    op = input("input stream id ")
    chat = pytchat.create(video_id=op)
    while True:
        while chat.is_alive():
            is_command = False
            for c in chat.get().sync_items():
                user_input = f"{c.message}"
                print(f"{c.datetime} [{c.author.name}] - {user_input}")
                for key in command_list["COMMANDS"]:
                    if user_input == key:
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
                    answer = chatbot.get_ai_response(user_input)
                    with open("answer.txt", "w", encoding="utf-8") as f:
                        f.write(f"{answer}")
                    print(answer)