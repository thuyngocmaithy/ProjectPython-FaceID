from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from Camera import Camera
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        # Tạo QLineEdit
        self.txtButton = QPushButton('Nhập mã sinh viên', self)
        self.lineEdit = QLineEdit(self)

        # Tạo QPushButton
        self.pushButton = QPushButton('OK', self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        # Tạo QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.txtButton)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)

    def on_pushButton_clicked(self):
        idSV = self.lineEdit.text()
        #print(idSV)
        # Xử lý idSV ở đây
        self.pushButton.clicked.connect(lambda: self.OpenCamera(idSV))
    def OpenCamera(self, id):
        # Tạo một đối tượng MainWindow để hiển thị video từ camera
        #print("đang mở camera")
        self.camera = Camera(id)
        self.camera.show()

if __name__ == '__main__':
    app = QApplication([])
    form = MyForm()
    form.show()
    app.exec()