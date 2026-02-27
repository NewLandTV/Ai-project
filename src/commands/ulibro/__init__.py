import ollama
import socket
from threading import Thread

prompt = "너는 MyLibro의 사서이자 인공지능이야. 사용자가 너에게 궁금하거나 도서 서비스를 이용하거나 이외의 용도로 대화해. 입력 데이터 형식은 다음과 같이 주어져. 'prompt|msg|mylib_json_data', prompt는 너의 역할이 담긴 글, msg는 사용자가 너에게 말하거나 도서 서비스를 이용하기 위한 말, mylib_json_data는 현재 도서관에 모든 도서 정보를 나타낸 것이야. 단, 책에 대한 잘못된 정보나 편향된 대답을 주지 않기 위해 인터넷 검색이나 너가 아는 선에서 책에 대한 간단한 스토리나 너의 생각, 사용자에 대답에 적절한 답을 해주면 돼. (mylib_json_data를 참고 및 분석하여 대답하면 좋음)"
messages = [{ "role": "system", "content": prompt }]
mylib_json_data = ""

def recv_message(sock: socket.socket):
    try:
        while True:
            data = sock.recv(65536).decode()
            data = data.split("|")
            if data[0] == "json":
                global mylib_json_data
                mylib_json_data = data[1]
    except ConnectionError:
        print("API 서버와 연결이 종료되었습니다.")
    except:
        print("API 서버에서 데이터를 수신하는 과정에서 예외가 발생했습니다.")

def client_run():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 8230))

        thread = Thread(target=recv_message, args=(sock,))
        thread.daemon = True
        thread.start()

        while True:
            msg = input("MyLibro에 대해서 AI 사서에게 물어보기... ('/exit'로 종료): ")
            if msg == "/exit":
                sock.send(msg.encode())
                break
            sock.send("/get lib".encode())

            messages.append({ "role": "user", "content": f"{prompt}|{msg}|{mylib_json_data}" })
            response = ollama.chat(model="exaone3.5", messages=messages)
            res = response.message.content
            messages.append({ "role": "assistant", "content": res })
            print(f"AI: {res}")
    except ConnectionAbortedError:
        print("API 서버에 연결할 수 없습니다.")
    except Exception as e:
        print(f"API 서버에 연결하는 도중에 예외가 발생했습니다. {e}")
    finally:
        sock.close()

def run():
    print("v0.2.0 ULibro 모듈이랍니다!")
    client_run()