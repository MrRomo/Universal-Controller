from PyQt5 import QtCore, QtGui, QtWidgets
from UI.QT_Engine import Ui_MainWindow
from time import sleep as delay
from Controller.Control import Control
from ConsoleManager import ConsoleManager
from MQTT_Engine import MQTTEngine
import threading
import sys
import json

class UniversalController():

    def __init__(self):
        self.ports = []
        self.MainWindow = None
        self.ui = None
        self.map_name = 'config.json'
        self.config = self.load_map()

    def load_map(self):
        with open(self.map_name) as json_file:
            return json.load(json_file)

    def save_map(self):
        with open(self.map_name, 'w') as f:
            json.dump(self.config, f)       

    def startApp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        app_icon = QtGui.QIcon()
        app_icon.addFile('Logo.jpg', QtCore.QSize(256,256))
        self.MainWindow.setWindowIcon(app_icon)
        self.MainWindow.show()
        #Start console
        self.console = self.ui.console
        self.console_manager = ConsoleManager(self.console)
        #Start mqtt
        self.mqtt_engine = MQTTEngine(self.config['broker'], self.console_manager.pub)
        self.mqtt_engine.connect()
        #Start control
        self.control = Control(self.config,self.ui, self.console_manager.pub, self.mqtt_engine.send_message)




if __name__ == "__main__":

    app = UniversalController()
    app.startApp()
    sys.exit(app.app.exec_())





    


