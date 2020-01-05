import sys
import threading

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import Controllers
import GUI
import HMI


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('rubber-duck.png'))
        self.HMI = HMI.HMI(self.ui)
        self.SetupConnections()

    def SetupConnections(self):
        self.ui.Home_PB.clicked.connect(self.HomePB)
        self.ui.GoTo_PushButton_1.clicked.connect(self.GoTo_PushButton_1)

    def HomePB(self):
        self.HMI.Input.Navigation_Req = 0

    def GoTo_PushButton_1(self):
        self.HMI.Input.Navigation_Req = 1

    def Supervisor(self, processor):
        self.HMI.ProcessEvents()
        self.HMI.ProcessData(processor)


class Processor(object):
    def __init__(self):
        self.controller = Controllers.RaspberryPiController()

    @threaded
    def CreateForm(self):
        self.form_app = QtWidgets.QApplication(sys.argv)
        self.form = Form()
        self.form.show()
        while True:
            self.form_app.processEvents()
            self.form.Supervisor(self)

    @threaded
    def TemporarySetup(self):
        self.controller.AddRobot('irox_Robot')
        while True:
            self.controller.RunRobot(self.controller.robot[0])


if __name__ == '__main__':
    processor = Processor()
    processor_proc = processor.TemporarySetup()
    form_proc = processor.CreateForm()
    processor_proc.join()
    form_proc.start()
