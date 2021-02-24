import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow
import os

from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))


        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        self.ui.pushButton_15.clicked.connect(self.ui.client)
        self.ui.pushButton_2.clicked.connect(self.ui.client)
        self.ui.lineEdit.returnPressed.connect(self.ui.client)

        self.ui.pushButton_11.clicked.connect(self.ui.file_selector)

        def save_name():
            namepath = os.getcwd()
            os.chdir(namepath)
            name = open('name.kos', 'w')
            name_text = self.ui.lineEdit_2.text()
            name.write(name_text)
            name.close()

        self.ui.lineEdit_2.returnPressed.connect(lambda: self.ui.label_7.setText(self.ui.lineEdit_2.text()))
        self.ui.lineEdit_2.returnPressed.connect(save_name)
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.label_7.setText(self.ui.lineEdit_2.text()))
        self.ui.pushButton_8.clicked.connect(save_name)

        def save_username():
            usernamenamepath = os.getcwd()
            os.chdir(usernamenamepath)
            username = open('username.kos', 'w')
            username_text = self.ui.lineEdit_3.text()
            username.write('@'+username_text)
            username.close()

        self.ui.lineEdit_3.returnPressed.connect(lambda: self.ui.label_8.setText('@'+self.ui.lineEdit_3.text()))
        self.ui.lineEdit_3.returnPressed.connect(save_username)
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.label_8.setText('@'+self.ui.lineEdit_3.text()))
        self.ui.pushButton_9.clicked.connect(save_username)
        


        self.ui.lineEdit_4.returnPressed.connect(self.ui.bio_edit)
        self.ui.lineEdit_4.returnPressed.connect(save_username)
        self.ui.pushButton_10.clicked.connect(self.ui.bio_edit)
        self.ui.pushButton_10.clicked.connect(save_username)



        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())