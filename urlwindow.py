# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urlwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UrlWindow(object):
    def setupUi(self, UrlWindow):
        UrlWindow.setObjectName("UrlWindow")
        UrlWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UrlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 100, 281, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Shreya/Downloads/download.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 300, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 440, 321, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        UrlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UrlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        UrlWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UrlWindow)
        self.statusbar.setObjectName("statusbar")
        UrlWindow.setStatusBar(self.statusbar)
        self.actionMain_Window = QtWidgets.QAction(UrlWindow)
        self.actionMain_Window.setObjectName("actionMain_Window")
        self.actionExit = QtWidgets.QAction(UrlWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionMain_Window)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(UrlWindow)
        QtCore.QMetaObject.connectSlotsByName(UrlWindow)

    def retranslateUi(self, UrlWindow):
        _translate = QtCore.QCoreApplication.translate
        UrlWindow.setWindowTitle(_translate("UrlWindow", "MainWindow"))
        self.pushButton.setText(_translate("UrlWindow", "Search An URL!"))
        self.label_2.setText(_translate("UrlWindow", "Say : Open \"website name\"!"))
        self.menuMenus.setTitle(_translate("UrlWindow", "Menus"))
        self.actionMain_Window.setText(_translate("UrlWindow", "Main Window!"))
        self.actionExit.setText(_translate("UrlWindow", "Exit!"))

