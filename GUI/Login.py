# Form implementation generated from reading ui file 'ui/Login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QCoreApplication
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from BUS.TaiKhoanBUS import TaiKhoanBUS
import main
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 590)
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 0, 801, 31))
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.btnClose = QtWidgets.QPushButton(parent=self.frame)
                self.btnClose.setGeometry(QtCore.QRect(777, 4, 24, 24))
                self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnClose.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("ui\\../image/close_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnClose.setIcon(icon)
                self.btnClose.setIconSize(QtCore.QSize(20, 20))
                self.btnClose.setObjectName("btnClose")
                self.btnMinimize = QtWidgets.QPushButton(parent=self.frame)
                self.btnMinimize.setGeometry(QtCore.QRect(752, 4, 24, 24))
                font = QtGui.QFont()
                font.setPointSize(6)
                self.btnMinimize.setFont(font)
                self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnMinimize.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("ui\\../image/subtract_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnMinimize.setIcon(icon1)
                self.btnMinimize.setIconSize(QtCore.QSize(20, 20))
                self.btnMinimize.setObjectName("btnMinimize")
                self.label_15 = QtWidgets.QLabel(parent=self.frame)
                self.label_15.setGeometry(QtCore.QRect(10, 2, 201, 26))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
                self.label_15.setFont(font)
                self.label_15.setAcceptDrops(False)
                self.label_15.setToolTip("")
                self.label_15.setAutoFillBackground(False)
                self.label_15.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_15.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.label_15.setScaledContents(False)
                self.label_15.setWordWrap(False)
                self.label_15.setIndent(-1)
                self.label_15.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
                self.label_15.setObjectName("label_15")
                self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(0, 30, 481, 561))
                font = QtGui.QFont()
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.frame_2.setFont(font)
                self.frame_2.setStyleSheet("background-image: url(./image/faceidDesign.png);")
                self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_2.setObjectName("frame_2")
                self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame_3.setGeometry(QtCore.QRect(480, 30, 321, 561))
                self.frame_3.setStyleSheet("#frame_3\n"
        "{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 92, 151, 255), stop:0.994318 rgba(54, 55, 149, 255));\n"
        "border:none;\n"
        "}")
                self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_3.setObjectName("frame_3")
                self.frame_4 = QtWidgets.QFrame(parent=self.frame_3)
                self.frame_4.setGeometry(QtCore.QRect(30, 60, 271, 461))
                self.frame_4.setStyleSheet("#frame_4\n"
        "{background-image: url(./image/boxShadow.png);\n"
        "}")
                self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_4.setObjectName("frame_4")
                self.label = QtWidgets.QLabel(parent=self.frame_4)
                self.label.setGeometry(QtCore.QRect(30, 38, 211, 51))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("#label\n"
        "{\n"
        "font-weight:bold;\n"
        "    color: rgb(0, 0, 127);\n"
        "}")
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
                self.label_2.setGeometry(QtCore.QRect(60, 130, 51, 16))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("#label_2\n"
        "{\n"
        "font-weight:bold;\n"
        "}")
                self.label_2.setObjectName("label_2")
                self.txtEmail = QtWidgets.QLineEdit(parent=self.frame_4)
                self.txtEmail.setGeometry(QtCore.QRect(60, 170, 151, 25))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txtEmail.setFont(font)
                self.txtEmail.setStyleSheet("#txtEmail\n"
        "{\n"
        "border: 2px solid rgb(0, 0, 127);\n"
        "border-radius: 5px;\n"
        "}")
                self.txtEmail.setObjectName("txtEmail")
                self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
                self.label_3.setGeometry(QtCore.QRect(60, 220, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("#label_3\n"
        "{\n"
        "font-weight:bold;\n"
        "}")
                self.label_3.setObjectName("label_3")
                self.txtPassword = QtWidgets.QLineEdit(parent=self.frame_4)
                self.txtPassword.setGeometry(QtCore.QRect(60, 260, 151, 25))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txtPassword.setFont(font)
                self.txtPassword.setStyleSheet("#txtPassword\n"
        "{\n"
        "border: 2px solid rgb(0, 0, 127);\n"
        "border-radius: 5px;\n"
        "}")
                self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                self.txtPassword.setObjectName("txtPassword")
                self.btnDangNhap = QtWidgets.QPushButton(parent=self.frame_4)
                self.btnDangNhap.setGeometry(QtCore.QRect(90, 350, 91, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.btnDangNhap.setFont(font)
                self.btnDangNhap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnDangNhap.setStyleSheet("#btnDangNhap\n"
        "{\n"
        "border-radius: 5px;\n"
        "border: 1px;\n"
        "background-color:rgb(0, 0, 127);\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "}\n"
        "#btnDangNhap:hover\n"
        "{\n"
        "background-color: rgb(0, 0, 175);\n"
        "}")
                self.btnDangNhap.setObjectName("btnDangNhap")
                self.btnDangNhap.clicked.connect(lambda: self.login_func(MainWindow))
                # Chọn minimize
                self.btnMinimize.clicked.connect(self.showMinimized)
                # Chọn close
                self.btnClose.clicked.connect(QCoreApplication.instance().quit)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_15.setText(_translate("MainWindow", "Phần mềm điểm danh sinh viên"))
                self.label.setText(_translate("MainWindow", "ĐĂNG NHẬP"))
                self.label_2.setText(_translate("MainWindow", "Email"))
                self.label_3.setText(_translate("MainWindow", "Password"))
                self.btnDangNhap.setText(_translate("MainWindow", "ĐĂNG NHẬP"))
        def showMinimized(self):
                MainWindow.showMinimized()
        def login_func(self, MainWindow):
                username = self.txtEmail.text()
                password = self.txtPassword.text()
                tk = TaiKhoanBUS()
                resultLogin = tk.checkLogin(username,password)
                if resultLogin != False:        
                        # QtWidgets.QApplication.closeAllWindows()          
                        self.window = QtWidgets.QMainWindow()
                        self.ui = main.mainGUI(resultLogin[0], resultLogin[1], resultLogin[2])                        
                        self.ui.mainUi(self.window,"home")
                        MainWindow.hide()
                        self.window.show()
                else:
                        QMessageBox.information(self.centralwidget,"Thông báo","Login thất bại")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
#     MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
