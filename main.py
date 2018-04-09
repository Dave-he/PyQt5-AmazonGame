#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from mainWindow import *


class MyMainWindow(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.initUI()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.setWindowTitle("Amazon game")
    myWin.show()
    sys.exit(app.exec_())
