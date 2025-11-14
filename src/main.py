import os
from chatbot import Chatbot
from obs import OBS
import VsPyYt
from dotenv import load_dotenv

load_dotenv()

def main():
    print("인공지능 버튜버가 오고 있습니다...")
    chatbot = Chatbot(model="exaone3.5")
    obs = OBS(
        os.getenv("obs_host"),
        os.getenv("obs_port"),
        os.getenv("obs_password")
    )
    obs.connect_obs_websocket()
    VsPyYt.start(chatbot, obs)

if __name__ == "__main__":
    main()