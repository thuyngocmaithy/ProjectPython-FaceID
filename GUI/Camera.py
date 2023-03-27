import os
import cv2 , time
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox

class Camera(QWidget):
    def __init__(self, id):
        super().__init__()
        self.idSV = id
        # Khởi tạo QLabel để hiển thị hình ảnh từ camera
        self.image_label = QLabel(self)
        self.image_label.resize(640, 480)

        # Khởi tạo camera
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Khởi tạo số ảnh đã chụp và tổng số ảnh cần chụp
        self.count = 0
        self.total = 30

        # Khởi tạo button để chụp ảnh
        self.btn_capture = QPushButton('Chụp ảnh', self)
        self.btn_capture.move(20, 100)
        self.btn_capture.clicked.connect(self.capture_image)

        # Khởi tạo timer để lấy dữ liệu từ camera
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(10)

        # Khởi tạo layout để chứa các widget
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_capture)
        self.setLayout(layout)

    def capture_image(self):
        while self.count < self.total:
            _, frame = self.capture.read()
            cv2.imwrite(f'./image/photo/{self.idSV}image{self.count}.jpg', frame)
            self.count += 1
            time.sleep(0.1)  # thời gian giữa mỗi lần chụp
        self.timer.stop()
        self.capture.release()
        #QApplication.quit()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Đã lấy xong ảnh của sinh viên")
        msg.setInformativeText("Vui lòng đóng cửa sổ chụp ảnh để tiếp tục chương trình")
        msg.setWindowTitle("thông báo")
        msg.exec()

    def display_video_stream(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        # Chuyển đổi từ OpenCV Mat sang QImage
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(image)

        # Hiển thị hình ảnh trên QLabel
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    window = Camera(id)
    window.show()
    app.exec()