#! /usr/bin/env python3
import sys
from PyQt4 import QtCore, QtGui

class startQT4(QtGui.QMainWindow):
    def __init__(self, parent = none):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
