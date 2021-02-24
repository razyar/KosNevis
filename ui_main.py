import socket
import shutil
import select
import errno
import os
import sys
import PySide2
from PySide2 import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from shutil import copyfile

path = os.getcwd()
sys.path.append(path)
os.chdir(os.getcwd())




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 521))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("QPushButton {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)

        self.Btn_Toggle.setText("")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_15.setGeometry(QtCore.QRect(320, 0, 61, 31))
        self.pushButton_15.setMinimumSize(QtCore.QSize(61, 31))
        self.pushButton_15.setMaximumSize(QtCore.QSize(61, 31))
        self.pushButton_15.setStyleSheet("\n"
"  border: 0px solid;\n"
" image: url(:/1/icons/Screenshot (22).png);\n"
"\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 68))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/1/icons/menu/image.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btn_page_3.setText("")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    image: url(:/1/icons/menu/image(2).png);\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
" background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btn_page_2.setText("")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"    \n"
"    image: url(:/1/icons/menu/image(1).png);\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btn_page_1.setText("")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_left_menu)
        self.pushButton_7.setMinimumSize(QtCore.QSize(70, 60))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/menu/image(3).png);\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.page_4)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 141))
        datapath = os.getcwd()
        os.chdir(datapath+'/data')
        photofile = open('photo.kos', 'r')
        photo = photofile.read()
        self.label.setStyleSheet("image: url(%s);" % photo)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"image: url(%s);\n"
"border: 0px solid;" % photo)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(170, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(170, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(320, 70, 51, 41))
        self.label_9.setStyleSheet("image: url(:/1/icons/menu/Screenshot (43).png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 260, 113, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(30, 30, 30);\n"
"\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 290, 113, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(30, 30, 30);\n"
"\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 320, 113, 21))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(30, 30, 30);\n"
"\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 260, 41, 21))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/cil-check-alt.png);\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
" background-color: rgb(15, 15, 15);\n"
"}\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(50, 260, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(50, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(50, 330, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(260, 290, 41, 21))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/cil-check-alt.png);\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
" background-color: rgb(15, 15, 15);\n"
"}\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 320, 41, 21))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/cil-check-alt.png);\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
" background-color: rgb(15, 15, 15);\n"
"}\n"
"")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(34, 180, 91, 23))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 15, 15);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
" background-color: rgb(30, 30, 30);\n"
"}\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_8.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(120, 130, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("image: url(:/1/icons/menu/Screenshot (46).png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 0, 71, 71))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    image: url(:/1/icons/menu/Screenshot (42).png);\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(260, 130, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("image: url(:/1/icons/menu/Screenshot (46).png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(390, 130, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("image: url(:/1/icons/menu/Screenshot (46).png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 220, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 220, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 220, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(-10, -6, 911, 411))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 661, 401))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"border: 0px solid;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit.setGeometry(QtCore.QRect(0, 410, 581, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(590, 410, 31, 23))
        self.pushButton.setStyleSheet("image: url(:/1/icons/cil-paperclip.png);\n"
"border: 0px solid;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 410, 31, 23))
        self.pushButton_2.setStyleSheet("image: url(:/1/icons/cil-cursor.png);\n"
"border: 0px solid;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

       

        namepath = os.getcwd()
        os.chdir(datapath+'/data')
        namefile = open('name.kos', 'r')
        global name
        name = namefile.read()
        self.label_7.setText(name)
        
        usernamepath = os.getcwd()
        os.chdir(datapath+'/data')
        usernamefile = open('username.kos', 'r')
        global username
        username = usernamefile.read()
        
        self.label_8.setText(username)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KosNevis"))
        self.label_3.setText(_translate("MainWindow", "Welcome to KosNevis..\nThis page will be available in next update."))

        self.label_10.setText(_translate("MainWindow", "Name:"))
        self.label_11.setText(_translate("MainWindow", "Username:"))
        self.label_12.setText(_translate("MainWindow", "Bio:"))
        self.pushButton_11.setText(_translate("MainWindow", "Change"))
        self.label_2.setText(_translate("MainWindow", "Channels"))
        self.pushButton_4.setText(_translate("MainWindow", "V A N D A L S"))
        self.pushButton_5.setText(_translate("MainWindow", "Podcasts"))
        self.pushButton_6.setText(_translate("MainWindow", "Musics"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">You:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p></body></html>"))

        

    
    def client(self):
        HEADER_LENGTH = 10

        IP = "127.0.0.1"
        PORT = 1234
        my_username = "razyar saeedian"


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        client_socket.connect((IP, PORT))
        print('connected')

        client_socket.setblocking(False)

        username = my_username.encode('utf-8')
        print('passed')
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        print('passed2')
        client_socket.send(username_header + username)
        print('passed3')
        while self.lineEdit.text():
            try:
                
                message = self.lineEdit.text()
                f = open('data.kos', 'a')
                f.write("\n"+ str(message))
                messages = QtCore.QFile("data.kos")
                if not messages.open(QtCore.QIODevice.ReadOnly):
                    QtGui.QMessageBox.information(None, 'info', messages.errorString())
                stream_messages = QtCore.QTextStream(messages)
                self.textEdit.setText(stream_messages.readAll())
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)
                self.lineEdit.setText("")
                client_socket.settimeout(0)
                break;
            except Exception as e:
                print('No new message', e)
            try:

                while True:


                    username_header = client_socket.recv(HEADER_LENGTH)


                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()


                    username_length = int(username_header.decode('utf-8').strip())


                    username = client_socket.recv(username_length).decode('utf-8')

                    message_header = client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = client_socket.recv(message_length).decode('utf-8')


                    print((f'{username} > {message}'))

            except IOError as e:

                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()


                continue

            except Exception as e:

                print('Reading error: '.format(str(e)))
                sys.exit()

    

    def file_selector(self):
        Tk().withdraw() 
        photo = askopenfilename()
        print('location: '+ photo)
        datapath = os.getcwd()
        os.chdir(datapath)
        photofile = open('photo.kos', 'w')
        photofile.write(photo)
        self.label.setStyleSheet("image: url(%s)};" % photo)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
        "image: url(%s);\n"
        "border: 0px solid;" % photo)


    def bio_edit(self):
        datapath = os.getcwd()
        os.chdir(datapath)
        bio = self.lineEdit_4.text()
        biofile = open('bio.kos', 'w')
        biofile.write(bio)
        biofile.close()



import qrc_rc
