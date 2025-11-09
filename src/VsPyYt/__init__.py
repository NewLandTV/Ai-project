import asyncio
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import chatbot  # import ../chatbot.py

while True:
    s = input("1: yt, 2: no yt ")
    if s == "1":
        from .vsyt import run
        break
    elif s == "2":
        from .vsnoyt import run
        break

asyncio.run(run(chatbot))