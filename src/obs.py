from obswebsocket import events, obsws, requests

class OBS:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.ws = None

    def __del__(self):
        self.disconnect_obs_websocket()

    def connect_obs_websocket(self):
        try:
            self.ws = obsws(self.host, self.port, self.password)

            # 이벤트 핸들러 (연결 및 끊기) 등록.
            self.ws.register(self.connect_obs_websocket, events.Connect)
            self.ws.register(self.disconnect_obs_websocket, events.Disconnect)

            self.ws.connect()   # OBS 연결하기.
            print(f"OBS WebSocket 연결됨 {self.host}:{self.port}")
        except Exception as e:
            print(f"OBS error: {e}")

    def disconnect_obs_websocket(self):
        if self.ws and self.ws.ws.connected:    # 연결된 상태이면 연결 끊기.
            self.ws.disconnect()
            self.ws = None
            print("OBS WebSocket 연결 해제됨.")

    def update_obs_text(self, text_source_name, new_text):
        if self.ws == None or not self.ws.ws.connected: # OBS WebSocket에 연결된 상태가 아니면 실행 종료.
            return
        try:
            self.ws.call(requests.SetInputSettings(
                inputName=text_source_name,
                inputSettings={
                    "text": new_text
                }
            ))
        except Exception as e:
            print(f"OBS error in update_obs_text: {e}")