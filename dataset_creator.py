from google_new import google_data_creator
import pindown_new as pn

from PyQt5 import QtCore, QtGui, QtWidgets
from pymsgbox import *
from threading import Thread
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword.setEnabled(True)
        self.keyword.setGeometry(QtCore.QRect(80, 120, 641, 51))
        self.keyword.setStyleSheet("background-color: rgb(85, 85, 255);\n"
            "font: 16pt \"Noto Sans Malayalam UI\";\n"
            "border: None;\n"
            "padding: 10px;")
        self.keyword.setText("")
        self.keyword.setObjectName("keyword")

        self.reshape = QtWidgets.QCheckBox(self.centralwidget)
        self.reshape.setGeometry(QtCore.QRect(290, 190, 121, 41))
        self.reshape.setStyleSheet("font: 12pt \"Noto Sans Malayalam UI\";\n"
            "border: None;\n"
            "padding: 10px;")
        self.reshape.setObjectName("reshape")

        self.resx = QtWidgets.QLineEdit(self.centralwidget)
        self.resx.setGeometry(QtCore.QRect(480, 190, 91, 41))
        self.resx.setObjectName("resx")

        self.resy = QtWidgets.QLineEdit(self.centralwidget)
        self.resy.setGeometry(QtCore.QRect(630, 190, 91, 41))
        self.resy.setObjectName("resy")

        self.xline = QtWidgets.QLineEdit(self.centralwidget)
        self.xline.setEnabled(False)
        self.xline.setGeometry(QtCore.QRect(590, 190, 21, 41))
        self.xline.setObjectName("xline")

        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setEnabled(False)
        self.title.setGeometry(QtCore.QRect(220, 40, 401, 41))
        self.title.setStyleSheet("color: rgb(170, 0, 0);\n"
            "font:  18pt \"Noto Sans\";\n"
            "text-align: center;\n"
            "border: None;")
        self.title.setObjectName("title")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(650, 136, 54, 21))
        self.label.setObjectName("label")

        self.google = QtWidgets.QPushButton(self.centralwidget)
        self.google.setGeometry(QtCore.QRect(80, 260, 291, 51))
        self.google.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.google.setStyleSheet("font: 14pt \"Noto Mono\";\n"
            "color: rgb(18, 18, 18);\n"
            "background-color: rgb(33, 150, 240);\n"
            "border: None;")
        self.google.setObjectName("google")

        self.pinterest = QtWidgets.QPushButton(self.centralwidget)
        self.pinterest.setGeometry(QtCore.QRect(430, 260, 291, 51))
        self.pinterest.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pinterest.setStyleSheet("font: 14pt \"Noto Mono\";\n"
            "color: rgb(18, 18, 18);\n"
            "background-color: rgb(233, 30, 99);\n"
            "border: None;")
        self.pinterest.setObjectName("pinterest")

        self.developer_info = QtWidgets.QLineEdit(self.centralwidget)
        self.developer_info.setEnabled(False)
        self.developer_info.setGeometry(QtCore.QRect(200, 430, 391, 41))
        self.developer_info.setStyleSheet("font: 16pt \"Noto Mono\";\n"
            "color: rgb(255, 85, 0);\n"
            "border: None;")
        self.developer_info.setObjectName("developer_info")

        self.numberl = QtWidgets.QLineEdit(self.centralwidget)
        self.numberl.setGeometry(QtCore.QRect(150, 190, 91, 41))
        self.numberl.setObjectName("numberl")

        self.progbar = QtWidgets.QProgressBar(self.centralwidget)
        self.progbar.setGeometry(QtCore.QRect(110, 350, 571, 41))
        self.progbar.setStyleSheet("")
        self.progbar.setProperty("value", 0)
        self.progbar.setObjectName("progbar")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(420, 200, 54, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 54, 21))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def controls(self,warn = True):
        keyword = self.keyword.text()
        numberl = self.numberl.text()
        reshape = self.reshape.checkState()
        shape = (self.resx.text(),self.resy.text())

        if keyword.isspace() or keyword == None or keyword == "":
            if warn:
                alert(text="You must type keyword!", title="Error!", button='OK')

            return False

        if not numberl.isnumeric() or int(numberl) <= 0:
            if warn:
                alert(text="You must type number as int that bigger than zero!", title="Error!", button='OK')

            return False

        if int(reshape) != 0:
            if shape[0] == None or shape[0] == "" or not shape[0].isnumeric() or int(shape[0]) <= 0 or shape[1] == None or shape[1] == "" or not shape[1].isnumeric() or int(shape[1]) <= 0:
                if warn:
                    alert(text="You must type shape as int that bigger than zero if you want to reshape!", title="Error!", button='OK')

                return False

        if reshape == 0:
            reshape = True

        if reshape == 1:
            reshape = False

        if shape[0] == "":
            shape = (0,0)

        return keyword,numberl,reshape,(int(shape[0]),int(shape[1]))

    def with_google(self):
        try:
            keyword, numberl, reshape, shape = self.controls()
        except Exception as e:
            print("Error")
            return
        self.progbar.setValue(0)
        print("Starting ...")
        self.google.setEnabled(False)
        self.pinterest.setEnabled(False)
        google_data_creator(keyword, int(int(numberl) + 75), reshape, shape,self.progbar)
        self.progbar.setValue(100)
        alert(text=f"{keyword} images downloaded from Google Images!", title="Done!", button='OK')
        self.progbar.setValue(0)
        self.google.setEnabled(True)
        self.pinterest.setEnabled(True)
        print("Done!")

    def with_pinterest(self):
        try:
            keyword, numberl, reshape, shape = self.controls()
        except Exception as e:
            print(e)
            return
        self.progbar.setValue(0)
        print("Starting ...")
        self.google.setEnabled(False)
        self.pinterest.setEnabled(False)
        Thread(target=lambda: pn.go(keyword, int(numberl), reshape, shape,self.progbar)).start()
        while not pn.bingo.DONE:
            time.sleep(1)

        self.progbar.setValue(100)
        alert(text=f"{keyword} images downloaded from Pinterest Images!", title="Done!", button='OK')
        self.progbar.setValue(0)
        self.google.setEnabled(True)
        self.pinterest.setEnabled(True)
        print("Done!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rayla Dataset Creator"))
        self.reshape.setText(_translate("MainWindow", "Reshape"))
        self.xline.setText(_translate("MainWindow", " X"))
        self.title.setText(_translate("MainWindow", "          RAYLA DATASET CREATOR"))
        self.label.setText(_translate("MainWindow", "Keyword"))
        self.google.setText(_translate("MainWindow", "Google Images"))
        self.pinterest.setText(_translate("MainWindow", "Pinterest Images"))
        self.developer_info.setText(_translate("MainWindow", "    DEVELOPER: @AANGFANBOY"))
        self.label_2.setText(_translate("MainWindow", "Shape ="))
        self.label_3.setText(_translate("MainWindow", "Number"))

        self.google.clicked.connect(self.with_google)
        self.pinterest.clicked.connect(self.with_pinterest)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

