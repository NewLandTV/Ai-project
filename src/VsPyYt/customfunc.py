from func import *
import time

async def spin2(websocket, x, y, s):
    for angle in range(0, 361, 30):
        await mdmv(websocket, 0.3, False, x, y, angle, s)
        time.sleep(0.1)

async def move(websocket, x, y, s):
    n = 3
    for p in range(-n, n + 1):
        for q in range(-n, n + 1):
            await mdmv(websocket, 0, False, x + p * 0.05, y + q * 0.05, 0, s)
            time.sleep(0.05)
    await mdmv(websocket, 0.2, False, x, y, 0, s)