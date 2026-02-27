import os
import sys
from chatbot import Chatbot
from obs import OBS
import VsPyYt
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    모드\n
    1: VTube Studio Mode\n
    2: CLI Mode\n
    3: GUI Mode (미구현)
    """
    if len(sys.argv) == 1:
        print("모드를 입력해 주세요.")
        return
    print("인공지능 버튜버가 오고 있습니다...")

    # 챗봇 설정
    chatbot = Chatbot(model="exaone3.5")

    # OBS 연동
    obs = OBS(
        os.getenv("obs_host"),
        os.getenv("obs_port"),
        os.getenv("obs_password")
    )
    obs.connect_obs_websocket()

    mode = int(sys.argv[1])

    if mode == 1:
        # Vtube Studio, YouTube 실시간 채팅창 연동
        VsPyYt.start(chatbot, obs)
    elif mode == 2:
        pass    # TODO: CLI 모드 구현 (VTube Studio 없이 실행할 수 있는 모드)
    else:
        print("GUI 모드는 구현되지 않았습니다.")

if __name__ == "__main__":
    main()