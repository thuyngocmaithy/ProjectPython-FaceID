from PyQt6 import QtGui, QtWidgets, QtCore
from pathlib import Path, PurePath
import sys
import home
import QuanLy
import QuanLySinhVien
import QuanLyBuoiHoc
import MatKhau
import NhanDien
import QuanLyDiemDanh
import ThongKe
import QuanLyGiangVien
import qdarkstyle
from PyQt6.QtCore import QCoreApplication
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
DarkMode = True


def listChangeStyleSheet_MD():
    ui.btnDark.setIcon(QtGui.QIcon("image/icon/moon_symbol_50px.png"))
    ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_20px.png"))    
    app.setStyleSheet(Path(
        r"C:\Users\thuyn\Documents\GitHub\ProjectPython-FaceID\GUI\qss\py_md_style.qss").read_text())


def listChangeStyleSheet_Dark():
    ui.btnDark.setIcon(QtGui.QIcon("image/icon/sun_50px.png"))
    ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_white_20px.png"))
    app.setStyleSheet(Path(
            r"C:\Users\thuyn\Documents\GitHub\ProjectPython-FaceID\GUI\qss\py_dark_style.qss").read_text())
 


def ChangeStyleDarkMode():
    if DarkMode:
        listChangeStyleSheet_MD()
    else:
        listChangeStyleSheet_Dark()


def ChangeDarkMode_UI():
    global DarkMode
    if DarkMode:
        listChangeStyleSheet_Dark()      
        DarkMode = False
    else:
        listChangeStyleSheet_MD()       
        DarkMode = True


def mainUi(page):
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    if page == "home":
        ui.stackedWidget.setCurrentWidget(ui.pageHome)
    elif page == "ql":
        ui.stackedWidget.setCurrentWidget(ui.pageQL)
    elif page == "mk":
        ui.stackedWidget.setCurrentWidget(ui.pageMK)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trang chủ
    ui.btnTrangChu.clicked.connect(Home_UI)
    # Chọn quản lý
    ui.btnQuanLy.clicked.connect(QuanLy_UI)
    # Chọn nhận diện
    ui.btnNhanDien.clicked.connect(NhanDien_UI)
    # Chọn mật khẩu
    ui.btnMatKhau.clicked.connect(MatKhau_UI)
    # Chọn thống kê
    ui.btnThongKe.clicked.connect(ThongKe_UI)
    #############################################
    # QUẢN LÝ
    #############################################
    # Chọn quản lý sinh viên
    ui.btnQLSV.clicked.connect(QLSV_UI)
    # Chọn quản lý buổi học
    ui.btnBuoiHoc.clicked.connect(QLBuoiHoc_UI)
    # Chọn quản lý điểm danh
    ui.btnDiemDanh.clicked.connect(QLDiemDanh_UI)
    # Chọn giảng viên
    ui.btnGiangVien.clicked.connect(QLGiangVien_UI)
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
   
    MainWindow.show()


def showMinimized():
    MainWindow.showMinimized()


def Home_UI():
    ui.stackedWidget.setCurrentWidget(ui.pageHome)


def QuanLy_UI():
    ui.stackedWidget.setCurrentWidget(ui.pageQL)


def MatKhau_UI():
    ui.stackedWidget.setCurrentWidget(ui.pageMK)


def QLSV_UI():
    global ui
    ui = QuanLySinhVien.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("ql"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


def QLGiangVien_UI():
    global ui
    ui = QuanLyGiangVien.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("ql"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


def QLBuoiHoc_UI():
    global ui
    ui = QuanLyBuoiHoc.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("ql"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


def QLDiemDanh_UI():
    global ui
    ui = QuanLyDiemDanh.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("ql"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


def ThongKe_UI():
    global ui
    ui = ThongKe.Ui_MainWindow()
    ui.setupUi(MainWindow)

    def ChangeTextDarkThongKe():
        ui.lbSoSV.setStyleSheet(
            'color:black;font-weight:bold;background-color:transparent; ')
        ui.lbSoLanVang.setStyleSheet(
            'color:black;font-weight:bold;background-color:transparent;')
        ui.lbSoBanDiemDanh.setStyleSheet(
            'color:black;font-weight:bold;background-color:transparent')
        ui.lbSoLanDiMuon.setStyleSheet(
            'color:black;font-weight:bold;background-color:transparent;')
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("home"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ChangeTextDarkThongKe()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    ui.btnDark.clicked.connect(ChangeTextDarkThongKe)
    MainWindow.show()


def NhanDien_UI():
    global ui
    ui = NhanDien.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(lambda: mainUi("home"))
    # Dark-Light Mode
    ChangeStyleDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


# def center(self):
#     qr = MainWindow.frameGeometry()
#     cp = MainWindow.screen().availableGeometry().center()
#     qr.moveCenter(cp)
#     MainWindow.move(qr.topLeft())
mainUi("home")
sys.exit(app.exec())
