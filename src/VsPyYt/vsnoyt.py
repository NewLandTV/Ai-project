import asyncio
import os
import setup
from setup import *
import websockets

if os.path.exists("customfunc.py"):
    import customfunc
    from customfunc import *

async def main():
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except Exception as e:
        print("Couldn't connect to vtube studio:", e)
        input("press enter to quit program")
        quit()
    command_list = await setup(websocket)
    while True:
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
asyncio.run(main())