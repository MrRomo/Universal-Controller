from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

from UI.QT_Engine import Ui_MainWindow, DialogApp
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
        self.config_name = 'config.json'
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_name) as json_file:
            return json.load(json_file)

    def save_config(self):
        with open(self.config_name, 'w') as outfile:
            json.dump(self.config, outfile)
        
    def init_control(self):
        self.config = self.load_config()
        self.control = Control(self.config,self.ui, self.console_manager.pub, self.mqtt_engine.send_message)
        
    def reload_control(self, config):
        self.config = config
        self.save_config()
        self.console_manager.pub('Reload Control\n')

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
        self.console_manager = ConsoleManager(self.ui.console)
        
        # Start Dialog
        self.ui.dialog = DialogApp(self.reload_control, self.config, self.console_manager.pub)
        
        #Start MQTT
        self.mqtt_engine = MQTTEngine(self.config['broker'], self.console_manager.pub, self.ui)

        #Start control
        threading.Thread(target=self.init_control, daemon=True).start()

if __name__ == "__main__":

    app = UniversalController()
    app.startApp()
    sys.exit(app.app.exec_())





    


