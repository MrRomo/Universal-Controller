from PyQt5 import QtCore, QtGui, QtWidgets
from UI.QT_Engine import Ui_MainWindow
from time import sleep as delay
import threading
import sys

class UniversalController():

    def __init__(self):
        self.ports = []
        self.MainWindow = None
        self.ui = None

    def startApp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        app_icon = QtGui.QIcon()
        app_icon.addFile('Logo.jpg', QtCore.QSize(256,256))
        self.MainWindow.setWindowIcon(app_icon)
        self.MainWindow.show()

    #     self.translate = self.ui.translate
    #     self.portSelector = self.ui.portSelector
    #     self.baudSelector = self.ui.baudSelector
    #     self.hexBox = self.ui.hexBox
    #     self.console = self.ui.console_thread

    #     #Buttons
    #     self.connectButton = self.ui.connectButton
    #     self.flashButton = self.ui.flashButton
    #     self.eraseButton = self.ui.eraseButton
    #     self.sendButton = self.ui.sendButton
    #     #acciotns
    #     self.openFile = self.ui.actionOpen

    #     # Init Managers 
    #     delay(1)
    #     self.consoleManager = ConsoleManager(self.console)
    #     self.serialManager = SerialManager(self.consoleManager, self.ui, self.app)
    #     self.fileManager = FileManager(self.hexBox, self.ui)
    #     self.burnerManager = BurnerManager(self.serialManager, self.fileManager, self.ui.progressBar, self.consoleManager)
    #     self.startSignals()
    #     self.startThreads()
        

    # def startThread(self, function):
    #     threading.Thread(target=function, daemon=True).start()
    
    # def startSignals(self):
    #     self.consoleManager.pub('Starting Signals\n')
    #     self.portSelector.currentIndexChanged.connect(self.serialManager.change_port)
    #     self.connectButton.clicked.connect(self.serialManager.connect)
    #     self.eraseButton.clicked.connect(self.serialManager.change_port)
    #     self.flashButton.clicked.connect(self.burnerManager.burn)
    #     self.sendButton.clicked.connect(self.serialManager.send_write)
    #     self.openFile.triggered.connect(self.fileManager.open_file)

    # def startThreads(self):
    #     self.startThread(self.serialManager.port_events)
    #     # self.startThread(self.serialManager.port_selector_observer)
    #     # self.startThread(self.serialManager.read_port)
    #     # self.startThread(self.burnerManager.burn_task)

    

if __name__ == "__main__":

    app = UniversalController()
    app.startApp()
    sys.exit(app.app.exec_())





    


