from PyQt5 import QtCore, QtGui, QtWidgets
from UI.QT_Engine import Ui_MainWindow
from time import sleep as delay
import threading
import sys
import pygame
import json
class UniversalController():

    def __init__(self):
        self.ports = []
        self.MainWindow = None
        self.ui = None
        self.map_name = 'buttons.json'
        self.map = self.load_map()

    def load_map(self):
        with open(self.map_name) as json_file:
            return json.load(json_file)

    def save_map(self):
        with open('buttons.json', 'w') as f:
            json.dump(self.map, f)       

    def startApp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        app_icon = QtGui.QIcon()
        app_icon.addFile('Logo.jpg', QtCore.QSize(256,256))
        self.MainWindow.setWindowIcon(app_icon)
        self.MainWindow.show()

    

if __name__ == "__main__":

    app = UniversalController()
    app.startApp()
    sys.exit(app.app.exec_())





    


