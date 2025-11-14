import asyncio

def start(chatbot, obs):
    while True:
        s = input("1: yt, 2: no yt ")
        if s == "1":
            from .vsyt import run
            break
        elif s == "2":
            from .vsnoyt import run
            break

    asyncio.run(run(chatbot, obs))