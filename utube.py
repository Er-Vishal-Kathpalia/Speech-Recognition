# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utube.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YoutubeWindow(object):
    def setupUi(self, YoutubeWindow):
        YoutubeWindow.setObjectName("YoutubeWindow")
        YoutubeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(YoutubeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 100, 281, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Shreya/Downloads/download.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 300, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 450, 321, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        YoutubeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YoutubeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        YoutubeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YoutubeWindow)
        self.statusbar.setObjectName("statusbar")
        YoutubeWindow.setStatusBar(self.statusbar)
        self.actionMain_Window = QtWidgets.QAction(YoutubeWindow)
        self.actionMain_Window.setObjectName("actionMain_Window")
        self.actionExit = QtWidgets.QAction(YoutubeWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionMain_Window)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(YoutubeWindow)
        QtCore.QMetaObject.connectSlotsByName(YoutubeWindow)

    def retranslateUi(self, YoutubeWindow):
        _translate = QtCore.QCoreApplication.translate
        YoutubeWindow.setWindowTitle(_translate("YoutubeWindow", "MainWindow"))
        self.pushButton.setText(_translate("YoutubeWindow", "Play Music On YouTube!"))
        self.label_2.setText(_translate("YoutubeWindow", "Say : Play \"Artist/Album Name\"!"))
        self.menuMenus.setTitle(_translate("YoutubeWindow", "Menus"))
        self.actionMain_Window.setText(_translate("YoutubeWindow", "Main Window!"))
        self.actionExit.setText(_translate("YoutubeWindow", "Exit!"))

