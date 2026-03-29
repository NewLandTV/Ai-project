import asyncio
from .program import run
import traceback

async def run_program(program_func, chatbot, obs):
    try:
        await program_func(chatbot, obs)
    except KeyboardInterrupt:
        print("인공지능 버튜버가 떠납니다...")
    except Exception as e:
        error_msg = traceback.format_exc()
        print("예외 발생:", error_msg)
        print(e)

def start(chatbot, obs):
    try:
        asyncio.run(run_program(run, chatbot, obs))
    except KeyboardInterrupt:
        print("인공지능 버튜버가 떠납니다...")
    except Exception as e:
        error_msg = traceback.format_exc()
        print("예외 발생:", error_msg)
        print(e)