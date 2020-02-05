import datetime
import os
import subprocess
import sys
import threading
import time

from PyQt5.QtCore import QProcess

from form import Ui_MainWindow
from PyQt5 import QtWidgets

class myapp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.process = QProcess(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.process.kill)

    def btnClicked(self):
        #os.system('python script.py')
        #os.spawnl(os.P_NOWAIT, 'python script.py')
        #proc = subprocess.Popen(['python','script.py'])
        #tr = TestThreading()
        #time.sleep(1)
        #print(datetime.datetime.now().__str__() + ' : First output')
        #time.sleep(2)
        #print(datetime.datetime.now().__str__() + ' : Second output')
        #thread = threading.Thread(target=self.run, args=())
        runstr = 'ping'
        args = ['localhost','-t']
        #self.process.finished.connect(self.onFinished)
        #self.process.start(runstr, args)
        self.process.setStandardOutputFile('C:\Learning\PythonLearning2\BackgroundRun\ping.log')
        self.process.start(runstr, args)
        #self.process.waitForFinished()
        #result = self.process.readAll()
        #self.process.close()

    def onFinished(self, exitCode, exitStatus):
        pass

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() + ' : Start task in the background')
            time.sleep(self.interval)


class TestThreading(object):
    def __init__(self, interval=10):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() + ' : Start task in the background')
            time.sleep(self.interval)



app = QtWidgets.QApplication([])
application = myapp()
application.show()
sys.exit(app.exec())

