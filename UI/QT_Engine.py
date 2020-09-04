# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Engine.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from .button_dialog import Dialog as Ui_Dialog 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 633)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.control_selector = QtWidgets.QComboBox(self.centralwidget)
        self.control_selector.setGeometry(QtCore.QRect(100, 20, 161, 31))
        self.control_selector.setObjectName("control_selector")
        self.control_selector.addItem("")
        self.controller_text = QtWidgets.QLabel(self.centralwidget)
        self.controller_text.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.controller_text.setFont(font)
        self.controller_text.setObjectName("controller_text")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(690, 20, 111, 31))
        self.connect_button.setObjectName("connect_button")
        self.message_counter_text = QtWidgets.QLabel(self.centralwidget)
        self.message_counter_text.setGeometry(QtCore.QRect(270, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.message_counter_text.setFont(font)
        self.message_counter_text.setObjectName("message_counter_text")
        self.message_counter_texbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_counter_texbox.setEnabled(True)
        self.message_counter_texbox.setGeometry(QtCore.QRect(410, 20, 131, 31))
        self.message_counter_texbox.setReadOnly(True)
        self.message_counter_texbox.setObjectName("message_counter_texbox")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(660, 100, 111, 21))
        self.button_5.setObjectName("button_5")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(680, 70, 111, 21))
        self.button_7.setObjectName("button_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-190, -70, 1190, 790))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Media/Controller.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.button_6.setObjectName("button_6")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(40, 100, 111, 21))
        self.button_4.setObjectName("button_4")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(640, 140, 51, 41))
        self.button_0.setObjectName("button_0")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(690, 200, 51, 41))
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(640, 250, 51, 41))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(590, 200, 51, 41))
        self.button_3.setObjectName("button_3")
        self.button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.button_11.setGeometry(QtCore.QRect(500, 300, 51, 41))
        self.button_11.setObjectName("button_11")
        self.axis_3_0 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_3_0.setGeometry(QtCore.QRect(500, 250, 51, 41))
        self.axis_3_0.setObjectName("axis_3_0")
        self.axis_2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_2_1.setGeometry(QtCore.QRect(560, 300, 51, 41))
        self.axis_2_1.setObjectName("axis_2_1")
        self.axis_3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_3_1.setGeometry(QtCore.QRect(500, 350, 51, 41))
        self.axis_3_1.setObjectName("axis_3_1")
        self.axis_2_0 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_2_0.setGeometry(QtCore.QRect(440, 300, 51, 41))
        self.axis_2_0.setObjectName("axis_2_0")
        self.axis_0_1 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_0_1.setGeometry(QtCore.QRect(330, 300, 51, 41))
        self.axis_0_1.setObjectName("axis_0_1")
        self.axis_0_0 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_0_0.setGeometry(QtCore.QRect(210, 300, 51, 41))
        self.axis_0_0.setObjectName("axis_0_0")
        self.button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.button_10.setGeometry(QtCore.QRect(270, 300, 51, 41))
        self.button_10.setObjectName("button_10")
        self.axis_1_0 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_1_0.setGeometry(QtCore.QRect(270, 250, 51, 41))
        self.axis_1_0.setObjectName("axis_1_0")
        self.axis_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.axis_1_1.setGeometry(QtCore.QRect(270, 350, 51, 41))
        self.axis_1_1.setObjectName("axis_1_1")
        self.hat_1_0 = QtWidgets.QPushButton(self.centralwidget)
        self.hat_1_0.setGeometry(QtCore.QRect(150, 250, 51, 41))
        self.hat_1_0.setObjectName("hat_1_0")
        self.hat_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.hat_1_1.setGeometry(QtCore.QRect(150, 150, 51, 41))
        self.hat_1_1.setObjectName("hat_1_1")
        self.hat_0_1 = QtWidgets.QPushButton(self.centralwidget)
        self.hat_0_1.setGeometry(QtCore.QRect(210, 200, 51, 41))
        self.hat_0_1.setObjectName("hat_0_1")
        self.hat_0_0 = QtWidgets.QPushButton(self.centralwidget)
        self.hat_0_0.setGeometry(QtCore.QRect(90, 200, 51, 41))
        self.hat_0_0.setObjectName("hat_0_0")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(550, 90, 51, 41))
        self.button_9.setObjectName("button_9")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(210, 90, 51, 41))
        self.button_8.setObjectName("button_8")
        self.frame_rate = QtWidgets.QLabel(self.centralwidget)
        self.frame_rate.setGeometry(QtCore.QRect(360, 410, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_rate.setFont(font)
        self.frame_rate.setObjectName("frame_rate")
        self.console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(200, 470, 411, 111))
        self.console.setReadOnly(True)
        self.console.setMaximumBlockCount(200)
        self.console.setObjectName("console")
        self.broker_addres = QtWidgets.QLineEdit(self.centralwidget)
        self.broker_addres.setEnabled(True)
        self.broker_addres.setGeometry(QtCore.QRect(550, 20, 131, 31))
        self.broker_addres.setReadOnly(False)
        self.broker_addres.setObjectName("broker_addres")
        self.frame_rate_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.frame_rate_textbox.setGeometry(QtCore.QRect(340, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame_rate_textbox.setFont(font)
        self.frame_rate_textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_rate_textbox.setObjectName("frame_rate_textbox")
        self.label.raise_()
        self.control_selector.raise_()
        self.controller_text.raise_()
        self.connect_button.raise_()
        self.message_counter_text.raise_()
        self.message_counter_texbox.raise_()
        self.button_5.raise_()
        self.button_7.raise_()
        self.button_6.raise_()
        self.button_4.raise_()
        self.button_0.raise_()
        self.button_1.raise_()
        self.button_2.raise_()
        self.button_3.raise_()
        self.button_11.raise_()
        self.axis_3_0.raise_()
        self.axis_2_1.raise_()
        self.axis_3_1.raise_()
        self.axis_2_0.raise_()
        self.axis_0_1.raise_()
        self.axis_0_0.raise_()
        self.button_10.raise_()
        self.axis_1_0.raise_()
        self.axis_1_1.raise_()
        self.hat_1_0.raise_()
        self.hat_1_1.raise_()
        self.hat_0_1.raise_()
        self.hat_0_0.raise_()
        self.button_9.raise_()
        self.button_8.raise_()
        self.frame_rate.raise_()
        self.console.raise_()
        self.broker_addres.raise_()
        self.frame_rate_textbox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.control_selector.setItemText(0, _translate("MainWindow", "Control 1"))
        self.controller_text.setText(_translate("MainWindow", "Controller"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.message_counter_text.setText(_translate("MainWindow", "Message Counter"))
        self.button_5.setText(_translate("MainWindow", "Gyro Rigth"))
        self.button_7.setText(_translate("MainWindow", "AUTONOMUS ON"))
        self.button_6.setText(_translate("MainWindow", "AUTONOMUS OFF"))
        self.button_4.setText(_translate("MainWindow", "Gyro Left"))
        self.button_0.setText(_translate("MainWindow", "STD"))
        self.button_1.setText(_translate("MainWindow", "SP1"))
        self.button_2.setText(_translate("MainWindow", "SP2"))
        self.button_3.setText(_translate("MainWindow", "SP3"))
        self.button_11.setText(_translate("MainWindow", "Center"))
        self.axis_3_0.setText(_translate("MainWindow", "h_up"))
        self.axis_2_1.setText(_translate("MainWindow", "h_rt"))
        self.axis_3_1.setText(_translate("MainWindow", "h_dw"))
        self.axis_2_0.setText(_translate("MainWindow", "h_lf"))
        self.axis_0_1.setText(_translate("MainWindow", "n/a"))
        self.axis_0_0.setText(_translate("MainWindow", "n/a"))
        self.button_10.setText(_translate("MainWindow", "n/a"))
        self.axis_1_0.setText(_translate("MainWindow", "n/a"))
        self.axis_1_1.setText(_translate("MainWindow", "n/a"))
        self.hat_1_0.setText(_translate("MainWindow", "bw"))
        self.hat_1_1.setText(_translate("MainWindow", "fw"))
        self.hat_0_1.setText(_translate("MainWindow", "n/a"))
        self.hat_0_0.setText(_translate("MainWindow", "n/a"))
        self.button_9.setText(_translate("MainWindow", "n/a"))
        self.button_8.setText(_translate("MainWindow", "n/a"))
        self.frame_rate.setText(_translate("MainWindow", "Frame rate"))
        self.frame_rate_textbox.setText(_translate("MainWindow", "20"))

    
class DialogApp(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    def getInteger(self, num):
        i, okPressed = QInputDialog.getInt(self, "Get integer","Percentage:", num, 0, 100, 4)
        if okPressed:
            print(i)

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 10.50, 0, 100, 10)
        d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 10.50, 0, 100, 10)
        if okPressed:
            print(d)
        
    def getChoice(self):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(self, "Get item","Color:", items, 0, False)
        if okPressed and item:
            print(item)

    def getText(self,text):
        text, okPressed = QInputDialog.getText(self, "Get text", text.name, QLineEdit.Normal, text.value)
        if okPressed and text != '':
            print(text)