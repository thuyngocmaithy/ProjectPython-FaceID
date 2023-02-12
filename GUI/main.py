from PyQt6 import QtGui, QtWidgets, QtCore
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
DarkMode = True
def listChangeStyleSheet_MD():
    ui.btnDark.setIcon(QtGui.QIcon("image/icon/moon_symbol_50px.png"))
    ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_20px.png"))
    try:
        getattr(ui.lblSV, 'property')    
    except AttributeError:
        print("Doesn't exist")                
    else:
        ui.lblSV.setStyleSheet('#lblSV{color:white;font-weight:bold;background-color: transparent;}')
        ui.lblBuoiHoc.setStyleSheet('#lblBuoiHoc{color:white;font-weight:bold;background-color: transparent;}')
        ui.lblStatusCam.setStyleSheet('#lblStatusCam{color:white;font-weight:bold;background-color: transparent;}')
    ui.frmHeader.setStyleSheet('#frmHeader{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255))}')
def listChangeStyleSheet_Dark():
    ui.btnDark.setIcon(QtGui.QIcon("image/icon/sun_50px.png"))
    ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_white_20px.png"))
    try:
        getattr(ui.lblSV, 'property')   
    except AttributeError:
        print("Doesn't exist")
    else:
        ui.lblSV.setStyleSheet('#lblSV{color:black;font-weight:bold;background-color: transparent;}')
        ui.lblBuoiHoc.setStyleSheet('#lblBuoiHoc{color:black;font-weight:bold;background-color: transparent;}')
        ui.lblStatusCam.setStyleSheet('#lblStatusCam{color:black;font-weight:bold;background-color: transparent;}')
    ui.frmHeader.setStyleSheet('#frmHeader{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 4, 40, 255), stop:0.994318 rgba(0, 66, 123, 255))}')
def ChangeIconDarkMode():
    print(DarkMode)
    if DarkMode:
        listChangeStyleSheet_MD()
    else:
        listChangeStyleSheet_Dark()
def ChangeDarkMode_UI():
    global DarkMode
    if DarkMode:
        listChangeStyleSheet_Dark()
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyqt6"))       
        DarkMode = False
    else:
        listChangeStyleSheet_MD()
        app.setStyleSheet('')
        DarkMode = True
def mainUi():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)   
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn quản lý
    ui.btnQuanLy.clicked.connect(QuanLy_UI)
    # Chọn nhận diện
    ui.btnNhanDien.clicked.connect(NhanDien_UI)
    # Chọn mật khẩu
    ui.btnMatKhau.clicked.connect(MatKhau_UI)
    # Chọn thống kê
    ui.btnThongKe.clicked.connect(ThongKe_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()

def showMinimized():
    MainWindow.showMinimized()

def QuanLy_UI():
    global ui
    ui = QuanLy.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trang chủ
    ui.btnTrangChu.clicked.connect(mainUi)
    # Chọn nhận diện
    ui.btnNhanDien.clicked.connect(NhanDien_UI)
     # Chọn mật khẩu
    ui.btnMatKhau.clicked.connect(MatKhau_UI)
    # Chọn thống kê
    ui.btnThongKe.clicked.connect(ThongKe_UI)
    # Chọn quản lý sinh viên
    ui.btnQLSV.clicked.connect(QLSV_UI)
    # Chọn quản lý buổi học
    ui.btnBuoiHoc.clicked.connect(QLBuoiHoc_UI)
    # Chọn quản lý điểm danh
    ui.btnDiemDanh.clicked.connect(QLDiemDanh_UI)
    # Chọn giảng viên
    ui.btnGiangVien.clicked.connect(QLGiangVien_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


def QLSV_UI():
    global ui
    ui = QuanLySinhVien.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(QuanLy_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
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
    ui.btnBack.clicked.connect(QuanLy_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
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
    ui.btnBack.clicked.connect(QuanLy_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
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
    ui.btnBack.clicked.connect(QuanLy_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()

def ThongKe_UI():
    global ui    
    ui = ThongKe.Ui_MainWindow()
    ui.setupUi(MainWindow) 
    def ChangeTextDarkThongKe():
        ui.lbSoSV.setStyleSheet('color:black;font-weight:bold;background-color:transparent; ')
        ui.lbSoLanVang.setStyleSheet('color:black;font-weight:bold;background-color:transparent;')
        ui.lbSoBanDiemDanh.setStyleSheet('color:black;font-weight:bold;background-color:transparent')
        ui.lbSoLanDiMuon.setStyleSheet('color:black;font-weight:bold;background-color:transparent;')
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trở về
    ui.btnBack.clicked.connect(QuanLy_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ChangeTextDarkThongKe()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    ui.btnDark.clicked.connect(ChangeTextDarkThongKe)
    MainWindow.show()


def MatKhau_UI():
    global ui
    ui = MatKhau.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Chọn minimize
    ui.btnMinimize.clicked.connect(showMinimized)
    # Chọn close
    ui.btnClose.clicked.connect(QCoreApplication.instance().quit)
    # Chọn trang chủ
    ui.btnTrangChu.clicked.connect(mainUi)
    # Chọn quản lý
    ui.btnQuanLy.clicked.connect(QuanLy_UI)
    # Chọn nhận diện
    ui.btnNhanDien.clicked.connect(NhanDien_UI)
     # Chọn mật khẩu
    ui.btnMatKhau.clicked.connect(MatKhau_UI)
    # Chọn thống kê
    ui.btnThongKe.clicked.connect(ThongKe_UI)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
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
    ui.btnBack.clicked.connect(mainUi)
    # Dark-Light Mode
    ChangeIconDarkMode()
    ui.btnDark.clicked.connect(ChangeDarkMode_UI)
    MainWindow.show()


mainUi()
sys.exit(app.exec())
