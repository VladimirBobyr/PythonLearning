from PyQt5 import QtCore, QtWidgets

import psutil

from form import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.process = QtCore.QProcess(self)
        self.ui.pushButton.clicked.connect(self.start_process)
        self.ui.pushButton_2.clicked.connect(self.stop_process)
        self._pid = -1

    @QtCore.pyqtSlot()
    def start_process(self):
        runstr = "ping"
        args = ["localhost", "-t"]
        self.process.setProgram(runstr)
        self.process.setArguments(args)
        ok, pid = self.process.startDetached()
        if ok:
            self._pid = pid

    @QtCore.pyqtSlot()
    def stop_process(self):
        if self._pid > 0:
            p = psutil.Process(self._pid)
            p.terminate()
            self._pid = -1

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    application = MyApp()
    application.show()
    sys.exit(app.exec_())