from chatbot import Chatbot
import VsPyYt

def main():
    print("인공지능 버튜버가 오고 있습니다...")
    chatbot = Chatbot(model="exaone3.5")
    VsPyYt.start(chatbot)

if __name__ == "__main__":
    main()