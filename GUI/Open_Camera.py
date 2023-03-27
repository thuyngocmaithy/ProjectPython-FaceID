import os
import time
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtMultimedia import QCamera, QCameraViewfinder, QCameraImageCapture
from PyQt6.QtCore import QTimer, QCameraInfo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Khởi tạo camera và viewfinder
        self.camera = QCamera(QCameraInfo.defaultCamera())
        self.camera.setViewfinder(QCameraViewfinder())

        # Thiết lập khả năng chụp ảnh
        self.image_capture = QCameraImageCapture(self.camera)
        self.camera.setCaptureMode(QCamera.CaptureModes.CaptureStillImage)
        self.camera.imageCapture().setCaptureDestination(QCameraImageCapture.CaptureDestinations.CaptureToFile)

        # Thiết lập nút bắt đầu chụp ảnh
        self.start_button = QPushButton("Bắt đầu chụp ảnh")
        self.start_button.clicked.connect(self.start_capture)

        # Thiết lập layout
        layout = QVBoxLayout()
        layout.addWidget(self.camera.viewfinder())
        layout.addWidget(self.start_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Thiết lập biến đếm số ảnh đã chụp
        self.count = 0

        # Bắt đầu camera
        self.camera.start()

    def start_capture(self):
        # Thiết lập timer để chụp ảnh
        self.timer = QTimer()
        self.timer.setInterval(1000) # Chụp ảnh mỗi giây
        self.timer.timeout.connect(self.take_picture)
        self.timer.start()

    def take_picture(self):
        # Chụp ảnh
        self.image_capture.capture()

        # Lưu ảnh vào thư mục "images"
        image_dir = "image\images\\"
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        # Chờ cho đến khi ảnh được lưu vào file
        while not self.image_capture.isReadyForCapture():
            time.sleep(0.1)

        image = self.image_capture.availableCaptures()[0]
        timestamp = int(time.time())
        filename = os.path.join(image_dir, f"image_{timestamp}.jpg")
        print(filename)
        image.save(filename)

        # Tăng biến đếm số ảnh đã chụp và kiểm tra nếu đã đủ 30 ảnh thì dừng timer và chụp ảnh
        self.count += 1
        if self.count >= 30:
            self.timer.stop()
            self.camera.stop()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
