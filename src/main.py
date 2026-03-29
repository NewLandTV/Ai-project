import os
import sys
from chatbot import Chatbot
from obs import OBS
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    모드\n
    1: VTube Studio Mode\n
    2: CLI Mode\n
    3: GUI Mode
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

    # 모드에 따라 프로그램 실행 분기
    mode = int(sys.argv[1])
    match mode:
        case 1: # Vtube Studio, YouTube 실시간 채팅창 연동
            from VsPyYt import start
        case 2: # VTube Studio 없이 인공지능 버튜버를 콘솔 환경에서 실행
            from cli import start
        case 3: # Ai Studio (GUI 환경)에서 인공지능 버튜버와 상호작용을 할 수 있는 공간
            from studio import start
        case _: # 이외의 경우는 잘못된 모드 선택이므로 프로그램을 종료함.
            return
    start(chatbot, obs)

if __name__ == "__main__":
    main()