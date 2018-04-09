# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from collections import namedtuple

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QDesktopWidget

class MainWindow(object):
    def __init__(self):
        self.config = namedtuple(
            "Config", ('size', 'start_x', 'start_y', 'gridsize'))\
            (10, 70, 100, 60)

    def initUI(self):
        self.setWindowIcon(QIcon('./images/gameIcon.ico'))
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)  # show of the screen center

    def setupUi(self, MainWindow):
        MainWindow.resize(1024, 768)

        self.text = 'Welcome to learn pyQt5'

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(800, 70, 200, 340))
        self.groupBox.setObjectName("groupBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 130, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 180, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(200, 60, 60, 30))
        self.timer.setObjectName("timeNumber")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 60, 60, 30))
        self.label.setObjectName("timeLaber")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(460, 60, 60, 30))
        self.lcdNumber.setObjectName("scoreNumber")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(425, 60, 60, 30))
        self.label2.setObjectName("scoreLaber")

        self.sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.sld.setGeometry(QtCore.QRect(540, 60, 60, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "选项"))
        self.pushButton_2.setText(_translate("MainWindow", "人机先手"))
        self.pushButton_3.setText(_translate("MainWindow", "人机后手"))
        self.pushButton.setText(_translate("MainWindow", "人人对战"))
        self.pushButton_4.setText(_translate("MainWindow", "悔棋"))
        self.label.setText(_translate("MainWindow", "时间:"))
        self.label2.setText(_translate("MainWindow", "分数:"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.drawMap(event, painter)
        painter.end()

    def drawMap(self, event, qp):
     #   x,y,c=1
       # pix =QPixmap()
        c = 1
        for i in range(self.config.size):
            for j in range(self.config.size):
                x = self.config.start_x + self.config.gridsize * i
                y = self.config.start_y + self.config.gridsize * j
                if(c > 0):
                    qp.setBrush(Qt.white)
                    qp.setPen(Qt.white)
                    qp.drawRect(x, y, self.config.gridsize, self.config.gridsize)
                else:
                    qp.setBrush(Qt.gray)
                    qp.setPen(Qt.gray)
                    qp.drawRect(x, y , self.config.gridsize, self.config.gridsize)
                c = -c
            c = -c





