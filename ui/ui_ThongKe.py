# Form implementation generated from reading ui file 'c:\Users\Duyen\OneDrive\Documents\github\ProjectPython-FaceID\ui\ThongKe.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frmHeader = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmHeader.setGeometry(QtCore.QRect(0, 30, 851, 51))
        self.frmHeader.setAccessibleName("")
        self.frmHeader.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frmHeader.setStyleSheet("#frmHeader{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255))}\n"
"")
        self.frmHeader.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmHeader.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmHeader.setLineWidth(1)
        self.frmHeader.setObjectName("frmHeader")
        self.label_3 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3\n"
"{\n"
"    font-weight:bold;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnBack = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnBack.setGeometry(QtCore.QRect(730, 12, 61, 23))
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBack.setObjectName("btnBack")
        self.label_2 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setToolTip("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnDark = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnDark.setGeometry(QtCore.QRect(680, 8, 31, 31))
        self.btnDark.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDark.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/moon_symbol_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDark.setIcon(icon)
        self.btnDark.setIconSize(QtCore.QSize(20, 20))
        self.btnDark.setObjectName("btnDark")
        self.btnTime = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnTime.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.btnTime.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnTime.setStyleSheet("#btnTime\n"
"{\n"
"background-color: transparent;\n"
"}")
        self.btnTime.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/time_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTime.setIcon(icon1)
        self.btnTime.setIconSize(QtCore.QSize(20, 20))
        self.btnTime.setObjectName("btnTime")
        self.label_3.raise_()
        self.btnBack.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.btnDark.raise_()
        self.btnTime.raise_()
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 761, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_2.setStyleSheet("#frame_2\n"
"{\n"
"background-color: rgb(213, 189, 213);\n"
"border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.pushButton.setStyleSheet("#pushButton\n"
"{\n"
"border:none;\n"
"background-color:transparent;\n"
"}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/Student Male_70px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.lbSoSV = QtWidgets.QLabel(parent=self.frame_2)
        self.lbSoSV.setGeometry(QtCore.QRect(70, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSoSV.setFont(font)
        self.lbSoSV.setStyleSheet("#label_5\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.lbSoSV.setObjectName("lbSoSV")
        self.lblResultSV = QtWidgets.QLabel(parent=self.frame_2)
        self.lblResultSV.setGeometry(QtCore.QRect(70, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblResultSV.setFont(font)
        self.lblResultSV.setStyleSheet("#lblResultSV\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"color:#C21A09;\n"
"}\n"
"")
        self.lblResultSV.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResultSV.setObjectName("lblResultSV")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_4.setStyleSheet("#frame_4\n"
"{\n"
"background-color: #FFD8B9;\n"
"border-radius:5px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 30, 41, 31))
        self.pushButton_2.setStyleSheet("#pushButton_2\n"
"{\n"
"border:none;\n"
"background-color:transparent;\n"
"}")
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/document_70px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lblResultDiemDanh = QtWidgets.QLabel(parent=self.frame_4)
        self.lblResultDiemDanh.setGeometry(QtCore.QRect(50, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblResultDiemDanh.setFont(font)
        self.lblResultDiemDanh.setStyleSheet("#lblResultDiemDanh\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"color:#C21A09;\n"
"}\n"
"")
        self.lblResultDiemDanh.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResultDiemDanh.setObjectName("lblResultDiemDanh")
        self.lbSoBanDiemDanh = QtWidgets.QLabel(parent=self.frame_4)
        self.lbSoBanDiemDanh.setGeometry(QtCore.QRect(50, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSoBanDiemDanh.setFont(font)
        self.lbSoBanDiemDanh.setStyleSheet("#label_8\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.lbSoBanDiemDanh.setObjectName("lbSoBanDiemDanh")
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_3.setStyleSheet("#frame_3\n"
"{\n"
"background-color: #F2ABB3;\n"
"border-radius:5px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbSoLanDiMuon = QtWidgets.QLabel(parent=self.frame_3)
        self.lbSoLanDiMuon.setGeometry(QtCore.QRect(60, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSoLanDiMuon.setFont(font)
        self.lbSoLanDiMuon.setStyleSheet("#label_10\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.lbSoLanDiMuon.setObjectName("lbSoLanDiMuon")
        self.lblResultDiMuon = QtWidgets.QLabel(parent=self.frame_3)
        self.lblResultDiMuon.setGeometry(QtCore.QRect(60, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblResultDiMuon.setFont(font)
        self.lblResultDiMuon.setStyleSheet("#lblResultDiMuon\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"color:#C21A09;\n"
"}\n"
"")
        self.lblResultDiMuon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResultDiMuon.setObjectName("lblResultDiMuon")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 30, 41, 31))
        self.pushButton_4.setStyleSheet("#pushButton_4\n"
"{\n"
"border:none;\n"
"background-color:transparent;\n"
"}")
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/hurry_70px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame.setStyleSheet("#frame\n"
"{\n"
"background-color: #B1CAE9;\n"
"border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
"{\n"
"border:none;\n"
"background-color:transparent;\n"
"}")
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/high_priority_message_70px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lblResultVang = QtWidgets.QLabel(parent=self.frame)
        self.lblResultVang.setGeometry(QtCore.QRect(70, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblResultVang.setFont(font)
        self.lblResultVang.setStyleSheet("#lblResultVang\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"color:#C21A09;\n"
"}\n"
"")
        self.lblResultVang.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResultVang.setObjectName("lblResultVang")
        self.lbSoLanVang = QtWidgets.QLabel(parent=self.frame)
        self.lbSoLanVang.setGeometry(QtCore.QRect(70, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbSoLanVang.setFont(font)
        self.lbSoLanVang.setStyleSheet("#label_13\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.lbSoLanVang.setObjectName("lbSoLanVang")
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 210, 761, 361))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_11.setGeometry(QtCore.QRect(10, 8, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("#label_11\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.label_11.setObjectName("label_11")
        self.cmbOptionFindDiMuon = QtWidgets.QComboBox(parent=self.frame_7)
        self.cmbOptionFindDiMuon.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.cmbOptionFindDiMuon.setObjectName("cmbOptionFindDiMuon")
        self.cmbOptionFindDiMuon.addItem("")
        self.txtFindDiMuon = QtWidgets.QLineEdit(parent=self.frame_7)
        self.txtFindDiMuon.setGeometry(QtCore.QRect(80, 30, 211, 20))
        self.txtFindDiMuon.setObjectName("txtFindDiMuon")
        self.btnExportDiMuon = QtWidgets.QPushButton(parent=self.frame_7)
        self.btnExportDiMuon.setGeometry(QtCore.QRect(300, 30, 56, 22))
        self.btnExportDiMuon.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnExportDiMuon.setStyleSheet("#btnExportDiMuon{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 3px;\n"
"}\n"
"#btnExportDiMuon:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.btnExportDiMuon.setObjectName("btnExportDiMuon")
        self.tbwDiMuon = QtWidgets.QTableWidget(parent=self.frame_7)
        self.tbwDiMuon.setGeometry(QtCore.QRect(10, 60, 351, 101))
        self.tbwDiMuon.setObjectName("tbwDiMuon")
        self.tbwDiMuon.setColumnCount(6)
        self.tbwDiMuon.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwDiMuon.setItem(0, 5, item)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(10, 8, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("#label_12\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.label_12.setObjectName("label_12")
        self.txtFindVang = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtFindVang.setGeometry(QtCore.QRect(80, 30, 211, 20))
        self.txtFindVang.setObjectName("txtFindVang")
        self.cmbOptionFindVang = QtWidgets.QComboBox(parent=self.frame_6)
        self.cmbOptionFindVang.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.cmbOptionFindVang.setObjectName("cmbOptionFindVang")
        self.cmbOptionFindVang.addItem("")
        self.btnExportVang = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnExportVang.setGeometry(QtCore.QRect(300, 30, 56, 22))
        self.btnExportVang.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnExportVang.setStyleSheet("#btnExportVang{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 3px;\n"
"}\n"
"#btnExportVang:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.btnExportVang.setObjectName("btnExportVang")
        self.tbwVang = QtWidgets.QTableWidget(parent=self.frame_6)
        self.tbwVang.setGeometry(QtCore.QRect(10, 60, 351, 101))
        self.tbwVang.setObjectName("tbwVang")
        self.tbwVang.setColumnCount(6)
        self.tbwVang.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwVang.setItem(0, 5, item)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.frame_5 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(10, 7, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("#label_15\n"
"{\n"
"font-weight:bold;\n"
"background-color:transparent;\n"
"}\n"
"")
        self.label_15.setObjectName("label_15")
        self.txtFindKhongDD = QtWidgets.QLineEdit(parent=self.frame_5)
        self.txtFindKhongDD.setGeometry(QtCore.QRect(80, 30, 211, 20))
        self.txtFindKhongDD.setObjectName("txtFindKhongDD")
        self.cmbOptionFindKhongDD = QtWidgets.QComboBox(parent=self.frame_5)
        self.cmbOptionFindKhongDD.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.cmbOptionFindKhongDD.setObjectName("cmbOptionFindKhongDD")
        self.cmbOptionFindKhongDD.addItem("")
        self.btnExportKhongDD = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnExportKhongDD.setGeometry(QtCore.QRect(300, 30, 56, 22))
        self.btnExportKhongDD.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnExportKhongDD.setStyleSheet("#btnExportKhongDD{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 3px;\n"
"}\n"
"#btnExportKhongDD:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.btnExportKhongDD.setObjectName("btnExportKhongDD")
        self.tbwKhongDD = QtWidgets.QTableWidget(parent=self.frame_5)
        self.tbwKhongDD.setGeometry(QtCore.QRect(10, 60, 351, 281))
        self.tbwKhongDD.setObjectName("tbwKhongDD")
        self.tbwKhongDD.setColumnCount(6)
        self.tbwKhongDD.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwKhongDD.setItem(0, 5, item)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.btnClose = QtWidgets.QPushButton(parent=self.frame_8)
        self.btnClose.setGeometry(QtCore.QRect(777, 4, 24, 24))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnClose.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/close_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnClose.setIcon(icon6)
        self.btnClose.setIconSize(QtCore.QSize(20, 20))
        self.btnClose.setObjectName("btnClose")
        self.btnMinimize = QtWidgets.QPushButton(parent=self.frame_8)
        self.btnMinimize.setGeometry(QtCore.QRect(752, 4, 24, 24))
        self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\Duyen\\OneDrive\\Documents\\github\\ProjectPython-FaceID\\ui\\../image/icon/subtract_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMinimize.setIcon(icon7)
        self.btnMinimize.setIconSize(QtCore.QSize(20, 20))
        self.btnMinimize.setObjectName("btnMinimize")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_16.setGeometry(QtCore.QRect(10, 2, 201, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.label_16.setFont(font)
        self.label_16.setAcceptDrops(False)
        self.label_16.setToolTip("")
        self.label_16.setAutoFillBackground(False)
        self.label_16.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_16.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_16.setScaledContents(False)
        self.label_16.setWordWrap(False)
        self.label_16.setIndent(-1)
        self.label_16.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Thống kế hệ thống"))
        self.btnBack.setText(_translate("MainWindow", "Trở về"))
        self.label_2.setText(_translate("MainWindow", "09:15:00"))
        self.label_4.setText(_translate("MainWindow", "02/02/2022"))
        self.lbSoSV.setText(_translate("MainWindow", "Số sinh viên"))
        self.lblResultSV.setText(_translate("MainWindow", "12"))
        self.lblResultDiemDanh.setText(_translate("MainWindow", "3"))
        self.lbSoBanDiemDanh.setText(_translate("MainWindow", "Số bản điểm danh"))
        self.lbSoLanDiMuon.setText(_translate("MainWindow", "Số lần đi muộn"))
        self.lblResultDiMuon.setText(_translate("MainWindow", "10"))
        self.lblResultVang.setText(_translate("MainWindow", "5"))
        self.lbSoLanVang.setText(_translate("MainWindow", "Số lần vắng"))
        self.label_11.setText(_translate("MainWindow", "Sinh viên đi muộn"))
        self.cmbOptionFindDiMuon.setItemText(0, _translate("MainWindow", "Mã SV"))
        self.btnExportDiMuon.setText(_translate("MainWindow", "Export"))
        item = self.tbwDiMuon.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã SV"))
        item = self.tbwDiMuon.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.tbwDiMuon.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lớp"))
        item = self.tbwDiMuon.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày"))
        item = self.tbwDiMuon.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID buổi học"))
        item = self.tbwDiMuon.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Trạng thái"))
        __sortingEnabled = self.tbwDiMuon.isSortingEnabled()
        self.tbwDiMuon.setSortingEnabled(False)
        item = self.tbwDiMuon.item(0, 0)
        item.setText(_translate("MainWindow", "3120410500"))
        item = self.tbwDiMuon.item(0, 1)
        item.setText(_translate("MainWindow", "abc"))
        item = self.tbwDiMuon.item(0, 2)
        item.setText(_translate("MainWindow", "DCT1200"))
        item = self.tbwDiMuon.item(0, 3)
        item.setText(_translate("MainWindow", "16/01/2023"))
        item = self.tbwDiMuon.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tbwDiMuon.item(0, 5)
        item.setText(_translate("MainWindow", "Đi muộn 50 phút"))
        self.tbwDiMuon.setSortingEnabled(__sortingEnabled)
        self.label_12.setText(_translate("MainWindow", "Sinh viên vắng"))
        self.cmbOptionFindVang.setItemText(0, _translate("MainWindow", "Mã SV"))
        self.btnExportVang.setText(_translate("MainWindow", "Export"))
        item = self.tbwVang.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã SV"))
        item = self.tbwVang.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.tbwVang.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lớp"))
        item = self.tbwVang.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày"))
        item = self.tbwVang.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID buổi học"))
        item = self.tbwVang.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Trạng thái"))
        __sortingEnabled = self.tbwVang.isSortingEnabled()
        self.tbwVang.setSortingEnabled(False)
        item = self.tbwVang.item(0, 0)
        item.setText(_translate("MainWindow", "3120410500"))
        item = self.tbwVang.item(0, 1)
        item.setText(_translate("MainWindow", "abc"))
        item = self.tbwVang.item(0, 2)
        item.setText(_translate("MainWindow", "DCT1200"))
        item = self.tbwVang.item(0, 3)
        item.setText(_translate("MainWindow", "16/01/2023"))
        item = self.tbwVang.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tbwVang.item(0, 5)
        item.setText(_translate("MainWindow", "Vắng"))
        self.tbwVang.setSortingEnabled(__sortingEnabled)
        self.label_15.setText(_translate("MainWindow", "Sinh viên không điểm danh"))
        self.cmbOptionFindKhongDD.setItemText(0, _translate("MainWindow", "Mã SV"))
        self.btnExportKhongDD.setText(_translate("MainWindow", "Export"))
        item = self.tbwKhongDD.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã SV"))
        item = self.tbwKhongDD.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.tbwKhongDD.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lớp"))
        item = self.tbwKhongDD.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày"))
        item = self.tbwKhongDD.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID buổi học"))
        item = self.tbwKhongDD.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Trạng thái"))
        __sortingEnabled = self.tbwKhongDD.isSortingEnabled()
        self.tbwKhongDD.setSortingEnabled(False)
        item = self.tbwKhongDD.item(0, 0)
        item.setText(_translate("MainWindow", "3120410500"))
        item = self.tbwKhongDD.item(0, 1)
        item.setText(_translate("MainWindow", "abc"))
        item = self.tbwKhongDD.item(0, 2)
        item.setText(_translate("MainWindow", "DCT1200"))
        item = self.tbwKhongDD.item(0, 3)
        item.setText(_translate("MainWindow", "16/01/2023"))
        item = self.tbwKhongDD.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tbwKhongDD.item(0, 5)
        item.setText(_translate("MainWindow", "Đi muộn 50 phút"))
        self.tbwKhongDD.setSortingEnabled(__sortingEnabled)
        self.label_16.setText(_translate("MainWindow", "Phần mềm điểm danh sinh viên"))
