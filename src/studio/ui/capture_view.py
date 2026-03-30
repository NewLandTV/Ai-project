import cv2
import numpy as np
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap

def crop_and_resize(img, crop_rect, new_size):
    x, y, w, h = crop_rect
    cropped = img[y:y + h, x:x + w]
    resized = cv2.resize(cropped, new_size)
    return resized

def remove_chroma(img):
    bgr = img[:, :, :3]

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 50, 50])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # 알파 채널 추가
    b, g, r = cv2.split(bgr)
    alpha = cv2.bitwise_not(mask)
    result = cv2.merge((b, g, r, alpha))
    return result

def to_qimage(img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

    h, w, _ = rgb_img.shape
    q_img = QImage(rgb_img, w, h, QImage.Format.Format_RGBA8888)

    return q_img

class CaptureView(QWidget):
    def __init__(self):
        super().__init__()

        # 캡처 대상
        self.cap = cv2.VideoCapture(2)  # OBS 가상 카메라 사용 (번호는 임의 지정)
        
        # 레이아웃 설정
        layout = QVBoxLayout(self)

        self.label = QLabel("모델 화면")
        self.label.setFixedSize(800, 800)
        self.label.setStyleSheet("background: transparent;")

        # 투명 화면 설정
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        layout.addWidget(self.label)
        
        # 타이머 (FPS)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)    # 약 30FPS

    def __del__(self):
        self.cap.release()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        
        pixmap = self.process_image(frame)
        self.label.setPixmap(pixmap)

    def process_image(self, frame):
        frame = crop_and_resize(
            frame,
            (160, 0, 480, 480),
            (self.label.width(), self.label.height())
        )
        frame = remove_chroma(frame)

        img = to_qimage(frame)

        pixmap = QPixmap.fromImage(img)
        pixmap =  pixmap.scaled(
            self.label.width(),
            self.label.height()
        )

        return pixmap