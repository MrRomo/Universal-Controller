# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Soy un popup")
        self.setFixedSize(200, 100)



class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(259, 163)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 120, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.parameter_textbox = QtWidgets.QLineEdit(Dialog)
        self.parameter_textbox.setGeometry(QtCore.QRect(120, 70, 113, 31))
        self.parameter_textbox.setObjectName("parameter_textbox")
        self.instruction_textbox = QtWidgets.QLineEdit(Dialog)
        self.instruction_textbox.setGeometry(QtCore.QRect(120, 30, 111, 31))
        self.instruction_textbox.setObjectName("instruction_textbox")
        self.instruction = QtWidgets.QLabel(Dialog)
        self.instruction.setGeometry(QtCore.QRect(20, 36, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.instruction.setFont(font)
        self.instruction.setObjectName("instruction")
        self.parameter = QtWidgets.QLabel(Dialog)
        self.parameter.setGeometry(QtCore.QRect(20, 74, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parameter.setFont(font)
        self.parameter.setObjectName("parameter")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.instruction.setText(_translate("Dialog", "Instruction"))
        self.parameter.setText(_translate("Dialog", "Parameter"))