from PyQt6 import QtGui, QtWidgets, QtCore
from pathlib import Path, PurePath
import sys
import Home
import QuanLySinhVien
import QuanLyBuoiHoc
import NhanDien
import QuanLyDiemDanh
import ThongKe
import QuanLyGiangVien
import QuanLyTaiKhoan
import Login
import qdarkstyle
from BUS.Quyen_ChucNangBUS import Quyen_ChucNangBUS
from PyQt6.QtCore import QCoreApplication
maquyen = ''
email = ''
password = ''
class mainGUI():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()        
    ui = ''
    DarkMode = True
    def __init__(self, email, password, maquyen):
        self.email = email
        self.password = password
        self.maquyen = maquyen
        
        
    def listChangeStyleSheet_MD(self):
        self.ui.btnDark.setIcon(QtGui.QIcon("image/icon/moon_symbol_50px.png"))
        self.ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_20px.png"))    
        self.app.setStyleSheet(Path(
            r"qss\py_md_style.qss").read_text())        


    def listChangeStyleSheet_Dark(self):
        self.ui.btnDark.setIcon(QtGui.QIcon("image/icon/sun_50px.png"))
        self.ui.btnTime.setIcon(QtGui.QIcon("image/icon/time_white_20px.png"))
        self.app.setStyleSheet(Path(
                r"qss\py_dark_style.qss").read_text())
        
    


    def ChangeStyleDarkMode(self):
        if self.DarkMode:
            self.listChangeStyleSheet_MD()
        else:
            self.listChangeStyleSheet_Dark()


    def ChangeDarkMode_UI(self):
        if self.DarkMode:
            self.listChangeStyleSheet_Dark()      
            self.DarkMode = False
        else:
            self.listChangeStyleSheet_MD()       
            self.DarkMode = True
    def mainUi(self, MainWindow ,page):
        self.ui = Home.UI_Home(self.email, self.password)
        self.MainWindow = MainWindow
        
        self.ui.setupUi(MainWindow)
    
        if page == "home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)
        elif page == "ql":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageQL)
        elif page == "mk":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageMK)
        self.checkFunctionInPermission(self.maquyen)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trang chủ
        self.ui.btnTrangChu.clicked.connect(self.Home_UI)
        # Chọn quản lý
        self.ui.btnQuanLy.clicked.connect(self.QuanLy_UI)
        # Chọn nhận diện
        self.ui.btnNhanDien.clicked.connect(lambda: self.NhanDien_UI(MainWindow))
        # Chọn mật khẩu
        self.ui.btnMatKhau.clicked.connect(self.MatKhau_UI)
        # Chọn thống kê
        self.ui.btnThongKe.clicked.connect(lambda: self.ThongKe_UI(MainWindow))
        # Chọn tài khoản
        self.ui.btnTaiKhoan.clicked.connect(lambda: self.TaiKhoan_UI(MainWindow))
        #############################################
        # QUẢN LÝ
        #############################################
        # Chọn quản lý sinh viên
        self.ui.btnQLSV.clicked.connect(lambda: self.QLSV_UI(MainWindow))
        # Chọn quản lý buổi học
        self.ui.btnBuoiHoc.clicked.connect(lambda: self.QLBuoiHoc_UI(MainWindow))
        # Chọn quản lý điểm danh
        self.ui.btnDiemDanh.clicked.connect(lambda: self.QLDiemDanh_UI(MainWindow))
        # Chọn giảng viên
        self.ui.btnGiangVien.clicked.connect(lambda: self.QLGiangVien_UI(MainWindow))
        # Chọn logout
        self.ui.btnLogout.clicked.connect(lambda: self.logout(MainWindow))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
    
        MainWindow.show()


    def showMinimized(self):
        MainWindow.showMinimized()


    def Home_UI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)


    def QuanLy_UI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageQL)


    def MatKhau_UI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMK)


    def QLSV_UI(self, MainWindow):
        self.ui = QuanLySinhVien.UI_QuanLySinhVien()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"ql"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()


    def QLGiangVien_UI(self, MainWindow):        
        self.ui = QuanLyGiangVien.UI_QuanLyGiangVien()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"ql"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()


    def QLBuoiHoc_UI(self, MainWindow):
        self.ui = QuanLyBuoiHoc.UI_QuanLyBuoiHoc()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"ql"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()


    def QLDiemDanh_UI(self, MainWindow):
        self.ui = QuanLyDiemDanh.UI_QuanLyDiemDanh()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)

        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"ql"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()

        

    def ThongKe_UI(self,MainWindow):
        self.ui = ThongKe.UI_ThongKe()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)

        def ChangeTextDarkThongKe():
            self.ui.lbSoSV.setStyleSheet(
                'color:black;font-weight:bold;background-color:transparent; ')
            self.ui.lbSoLanVang.setStyleSheet(
                'color:black;font-weight:bold;background-color:transparent;')
            self.ui.lbSoBanDiemDanh.setStyleSheet(
                'color:black;font-weight:bold;background-color:transparent')
            self.ui.lbSoLanDiMuon.setStyleSheet(
                'color:black;font-weight:bold;background-color:transparent;')
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"home"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        ChangeTextDarkThongKe()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        self.ui.btnDark.clicked.connect(ChangeTextDarkThongKe)
        MainWindow.show()


    def NhanDien_UI(self, MainWindow):
        self.ui = NhanDien.UI_NhanDien()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"home"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()
    def TaiKhoan_UI(self, MainWindow):
        self.ui = QuanLyTaiKhoan.UI_QuanLyTaiKhoan()
        self.MainWindow = MainWindow
        self.ui.setupUi(MainWindow)
        # Chọn minimize
        self.ui.btnMinimize.clicked.connect(self.showMinimized)
        # Chọn close
        self.ui.btnClose.clicked.connect(lambda: sys.exit(self.app.exit()))
        # Chọn trở về
        self.ui.btnBack.clicked.connect(lambda: self.mainUi(MainWindow,"home"))
        # Dark-Light Mode
        self.ChangeStyleDarkMode()
        self.ui.btnDark.clicked.connect(self.ChangeDarkMode_UI)
        MainWindow.show()    
    def logout(self, MainWindow):
        
        # QtWidgets.QApplication.closeAllWindows()
        self.MainWindow = MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.DarkMode = True
        self.app.setStyleSheet(Path(
            r"qss\py_md_style.qss").read_text())                     
        MainWindow.hide()
        self.window.show()

    def checkFunctionInPermission(self, maquyen):
        qcn = Quyen_ChucNangBUS()
        listcn = qcn.getListChucNangTheoQuyen(maquyen) 
        if ('CN001' or 'CN002' or 'CN003' or 'CN004') in listcn:
            if 'CN001' not in listcn:
                self.ui.btnQLSV.hide()
            if 'CN002' not in listcn:
                self.ui.btnDiemDanh.hide()                
            if 'CN003' not in listcn:
                self.ui.btnGiangVien.hide() 
            if 'CN004' not in listcn:
                self.ui.btnBuoiHoc.hide()
                           
        else:
            self.ui.btnQuanLy.hide()
        if 'CN005' not in listcn:
            self.ui.btnNhanDien.hide()
        if 'CN006' not in listcn:
            self.ui.btnThongKe.hide()
        if 'CN007' not in listcn:
            self.ui.btnTaiKhoan.hide()
        if 'CN008' not in listcn:
            self.ui.btnMatKhau.hide()
        



    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    ui = mainGUI('admin@gmail.com','12345678','Q001')
    ui.mainUi(MainWindow, "home")
    MainWindow.show()
    sys.exit(app.exec())

