# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests


class Ui_MainWindow(object):

    def submit(self):
        try:
            amount = float(self.amount.text())
            convert_from = self.convertFrom.text()
            convert_to = self.convertTo.text()

            url = "https://v3.exchangerate-api.com/pair/93f0c026daefeb339637cca9/" + convert_from + "/" + convert_to

            response = requests.get(url)
            data = response.json()
            results = data["rate"] * amount
            self.result.setPlainText("{} {} = {} {}".format(amount, convert_from, results, convert_to))
        except:
            self.show_popup("Warning", "Check currency code or empty value", QMessageBox.Warning)

    def show_popup(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 381)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 104, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 35, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.convertFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.convertFrom.setGeometry(QtCore.QRect(73, 117, 62, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setUnderline(False)
        self.convertFrom.setFont(font)
        self.convertFrom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.convertFrom.setObjectName("convertFrom")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(239, 117, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setUnderline(False)
        self.amount.setFont(font)
        self.amount.setStyleSheet("\n"
                                  "background-color: rgb(255, 255, 255);")
        self.amount.setText("")
        self.amount.setObjectName("amount")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 18, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.convertTo = QtWidgets.QLineEdit(self.centralwidget)
        self.convertTo.setGeometry(QtCore.QRect(72, 166, 62, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setUnderline(False)
        self.convertTo.setFont(font)
        self.convertTo.setStyleSheet("\n"
                                     "background-color: rgb(255, 255, 255);")
        self.convertTo.setObjectName("convertTo")
        self.result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(50, 250, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result.setObjectName("result")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(140, 210, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.convert.setObjectName("convert")
        #############################################################################
        self.convert.clicked.connect(self.submit)
        #############################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.label.setText(_translate("MainWindow", "CURRENCY CONVERTER"))
        self.label_2.setText(_translate("MainWindow", "CURRENCY CODE"))
        self.label_3.setText(_translate("MainWindow", "AMOUNT"))
        self.label_4.setText(_translate("MainWindow", "From:"))
        self.label_5.setText(_translate("MainWindow", "To:"))
        self.convert.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
