import asyncio
import os
import pytchat
from pytchat import *
import setup
from setup import *
import websockets

if os.path.exists("customfunc.py"):
    import customfunc
    from customfunc import *

async def main():
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    command_list = await setup(websocket)
    ###############################################
    #         Main loops for yt                   #
    ###############################################
    op = input("input stream id ")
    chat = pytchat.create(video_id=op)
    while True:
        while chat.is_alive():
            for c in chat.get().sync_items():
                print(f"{c.datetime} [{c.author.name}] - {c.message}")
                for key in command_list["COMMANDS"]:
                    if f"{c.message}" == key:
                        mdinf = await getmd(websocket)
                        s = mdinf["data"]["modelPosition"]["size"]
                        r = mdinf["data"]["modelPosition"]["rotation"]
                        x = mdinf["data"]["modelPosition"]["positionX"]
                        y = mdinf["data"]["modelPosition"]["positionY"]
                        cm = command_list["COMMANDS"][key]
                        await eval(cm)
asyncio.run(main())