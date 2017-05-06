#! /usr/bin/env python3
# statusbar 实验

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 100, 450, 450)
        self.setWindowTitle('First StatusBar')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
