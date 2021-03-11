# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NovelWindow(object):
    def setupUi(self, NovelWindow):
        NovelWindow.setObjectName("NovelWindow")
        NovelWindow.resize(739, 632)
        self.centralwidget = QtWidgets.QWidget(NovelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 130, 621, 361))
        self.listWidget.setToolTip("")
        self.listWidget.setToolTipDuration(2)
        self.listWidget.setFrameShape(QtWidgets.QFrame.HLine)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 520, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 520, 101, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 520, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 520, 101, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        NovelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NovelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        NovelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NovelWindow)
        self.statusbar.setObjectName("statusbar")
        NovelWindow.setStatusBar(self.statusbar)
        self.actionMainWindow = QtWidgets.QAction(NovelWindow)
        self.actionMainWindow.setObjectName("actionMainWindow")
        self.actionExit = QtWidgets.QAction(NovelWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionMainWindow)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(NovelWindow)
        QtCore.QMetaObject.connectSlotsByName(NovelWindow)

    def retranslateUi(self, NovelWindow):
        _translate = QtCore.QCoreApplication.translate
        NovelWindow.setWindowTitle(_translate("NovelWindow", "MainWindow"))
        self.label.setText(_translate("NovelWindow", "Listen A Novel!"))
        self.pushButton.setText(_translate("NovelWindow", "Load A Novel!"))
        self.pushButton_2.setText(_translate("NovelWindow", "Read A Novel!"))
        self.pushButton_3.setText(_translate("NovelWindow", "Listen A Novel!"))
        self.pushButton_4.setText(_translate("NovelWindow", "Cancel!"))
        self.menuMenus.setTitle(_translate("NovelWindow", "Menus"))
        self.actionMainWindow.setText(_translate("NovelWindow", "MainWindow!"))
        self.actionExit.setText(_translate("NovelWindow", "Exit!"))

