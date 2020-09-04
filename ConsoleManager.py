from PyQt5 import QtCore, QtGui, QtWidgets  
from collections import deque as dq 
from datetime import datetime
from time import sleep as delay
from datetime import datetime 
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from collections import deque as dq 

class QueueThread(QThread):
    # Create a counter thread
    change_value = pyqtSignal(str)
    def run(self):
        self.queue = dq(maxlen = 200)
        while 1:
            if(len(self.queue)):
                msg = self.queue[0]
                self.queue.popleft()                
                self.change_value.emit(msg)
            delay(0.01)


class ConsoleManager():
    def __init__(self, console):
        self.console = console
        self.console_thread = QueueThread()
        self.console_thread.change_value.connect(self.updateConsole)
        self.console_thread.start()
        delay(.1)
        self.pub('Starting Console Manager\n')

    def pub (self, msg):
        self.console_thread.queue.append(msg)
        return 0
        
    def updateConsole(self, msg):
        time = datetime.now()
        msg = time.strftime("%H:%M:%S.%f  ") + msg
        self.console.moveCursor(QtGui.QTextCursor.End)
        self.console.ensureCursorVisible()
        self.console.insertPlainText(msg)
