import socket
from threading import Thread

def recv_message(sock: socket.socket):
    try:
        while True:
            data = sock.recv(1024)
            print(f"API 서버에서 수신한 데이터 : {data.decode()}")
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
            msg = input("API 서버로 보낼 메시지 입력 ('/exit'로 종료): ")
            sock.send(msg.encode())
            if msg == "/exit":
                break
    except ConnectionAbortedError:
        print("API 서버에 연결할 수 없습니다.")
    except Exception as e:
        print(f"API 서버에 연결하는 도중에 예외가 발생했습니다. {e}")
    finally:
        sock.close()

def run():
    """
    TODO: MyLibro와 연동하여 Ai project에서 MyLibro의 데이터를 접근 -> 도서 데이터를 처리함.
    Ai가 도서 데이터를 프롬프트로 명령을 처리하여 행동한 후의 결과를 대상에게 보냄.
    """
    print("v0.1.1 ULibro 모듈이랍니다!")
    client_run()