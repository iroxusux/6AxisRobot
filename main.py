import sys
import multiprocessing

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import Controllers
import GUI
import HMI


def threaded(fn):
    def wrapper(*args):
        process = multiprocessing.Process(target=fn, args=args)
        process.start()
        return process
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

    def Supervisor(self, queue):
        if not queue.empty():
            processor = queue.get()
            self.HMI.ProcessEvents()
            self.HMI.ProcessData(processor)


class Processor(object):
    def __init__(self):
        self.controller = Controllers.RaspberryPiController()


def HandleProcessor(processor, queue):
    processor.controller.AddRobot('irox_Robot')
    while True:
        processor.controller.RunRobot(processor.controller.robot[0])
        queue.put(processor)


def HandleForm(queue):
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    while True:
        app.processEvents()
        form.Supervisor(queue)


if __name__ == '__main__':
    processor = Processor()
    queue = multiprocessing.Queue()
    proc1 = multiprocessing.Process(target=HandleProcessor, args=(processor, queue))
    proc2 = multiprocessing.Process(target=HandleForm, args=(queue,))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
