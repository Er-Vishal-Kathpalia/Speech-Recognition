# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_computerwindow(object):
    def setupUi(self, computerwindow):
        computerwindow.setObjectName("computerwindow")
        computerwindow.resize(640, 294)
        self.centralwidget = QtWidgets.QWidget(computerwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.commandLinkButton_2)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.commandLinkButton_3)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton_4)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.commandLinkButton_5)
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 621, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        computerwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(computerwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        computerwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(computerwindow)
        self.statusbar.setObjectName("statusbar")
        computerwindow.setStatusBar(self.statusbar)
        self.actionMainWindow = QtWidgets.QAction(computerwindow)
        self.actionMainWindow.setObjectName("actionMainWindow")
        self.actionExit = QtWidgets.QAction(computerwindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionMainWindow)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menuMenus.addSeparator()
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(computerwindow)
        QtCore.QMetaObject.connectSlotsByName(computerwindow)

    def retranslateUi(self, computerwindow):
        _translate = QtCore.QCoreApplication.translate
        computerwindow.setWindowTitle(_translate("computerwindow", "MainWindow"))
        self.commandLinkButton_2.setText(_translate("computerwindow", "Say: \'Open Settings!\'"))
        self.commandLinkButton.setText(_translate("computerwindow", "Say : \'Open Explorer!\'"))
        self.commandLinkButton_3.setText(_translate("computerwindow", "Say : \'Open MS Word!\'"))
        self.commandLinkButton_4.setText(_translate("computerwindow", "Say : \'Open WinAmp!\'"))
        self.commandLinkButton_5.setText(_translate("computerwindow", "Say : \'Open Calculator!\'"))
        self.commandLinkButton_6.setText(_translate("computerwindow", "Say : \'Open Calendar!\'"))
        self.pushButton.setText(_translate("computerwindow", "Press N Speak!"))
        self.menuMenus.setTitle(_translate("computerwindow", "Menus"))
        self.actionMainWindow.setText(_translate("computerwindow", "MainWindow!"))
        self.actionExit.setText(_translate("computerwindow", "Exit!"))

