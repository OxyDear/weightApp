# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'push.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys


class Ui_WindowPush(QMainWindow):
    def setupUi(self, WindowPush):
        self.res = 0
        WindowPush.setObjectName("WindowPush")
        WindowPush.resize(240, 240)
        WindowPush.setMinimumSize(QtCore.QSize(240, 240))
        WindowPush.setMaximumSize(QtCore.QSize(240, 240))
        self.centralwidget = QtWidgets.QWidget(WindowPush)
        self.centralwidget.setObjectName("centralwidget")
        self.res_q = QtWidgets.QLabel(self.centralwidget)
        self.res_q.setGeometry(QtCore.QRect(60, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.res_q.setFont(font)
        self.res_q.setObjectName("res_q")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 90, 110, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 70, 31))
        # self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton2.setGeometry(QtCore.QRect(80, 150, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        # self.pushButton2.setFont(font)
        # self.pushButton2.setObjectName("pushButton")
        WindowPush.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowPush)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        WindowPush.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowPush)
        self.statusbar.setObjectName("statusbar")
        WindowPush.setStatusBar(self.statusbar)

        self.retranslateUi(WindowPush)
        QtCore.QMetaObject.connectSlotsByName(WindowPush)

        self.adder(WindowPush)

    def retranslateUi(self, WindowPush):
        _translate = QtCore.QCoreApplication.translate
        WindowPush.setWindowTitle(_translate("WindowPush", "MainWindow"))
        self.res_q.setText(_translate("WindowPush", "What result?"))
        self.pushButton.setText(_translate("WindowPush", "PUSH"))
        # self.pushButton2.setText(_translate("WindowPush", "EXIT"))

    def adder(self, WindowPush):
        self.pushButton.clicked.connect(lambda: self.push(WindowPush))

    def push(self, window):
        self.res = self.lineEdit.text()
        window.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WindowPush = QtWidgets.QMainWindow()
    ui = Ui_WindowPush()
    ui.setupUi(WindowPush)
    WindowPush.show()
    sys.exit(app.exec_())