from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os

class ViewImage(QMainWindow):
    def __init__(self , id):
        super().__init__()
        self.setWindowTitle("Hiển thị ảnh")
        idSV = id
        # Tạo widget chính để đặt lưới ảnh
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Lặp qua 30 ảnh và đặt vào lưới
        for i in range(30):
            # Tạo QLabel để hiển thị ảnh
            label = QLabel(self)
            label.setFixedSize(120, 100) # đặt kích thước cho label
            label.setAlignment(Qt.AlignmentFlag.AlignCenter) # căn giữa ảnh trong label
            
            # Tạo đối tượng QPixmap từ file ảnh
            file_path = os.path.join("image\photo\\"+ idSV+'image'+str(i)+'.jpg')
            pixmap = QPixmap(file_path)
            
            # Thay đổi kích thước của ảnh
            scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            # Đặt ảnh vào QLabel
            label.setPixmap(scaled_pixmap)
            
            # Đặt QLabel vào ô tương ứng trong lưới
            row = i // 6 # mỗi hàng có 5 ảnh
            col = i % 6
            grid_layout.addWidget(label, row, col)

if __name__ == "__main__":
    app = QApplication([])
    window = ViewImage(id)
    window.show()
    app.exec()