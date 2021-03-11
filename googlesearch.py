# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'googlesearch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_googlewindow(object):
    def setupUi(self, googlewindow):
        googlewindow.setObjectName("googlewindow")
        googlewindow.resize(800, 600)
        googlewindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(googlewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 281, 161))
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
        self.label_2.setGeometry(QtCore.QRect(230, 440, 321, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        googlewindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(googlewindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menumenus = QtWidgets.QMenu(self.menubar)
        self.menumenus.setObjectName("menumenus")
        googlewindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(googlewindow)
        self.statusbar.setObjectName("statusbar")
        googlewindow.setStatusBar(self.statusbar)
        self.actionmain = QtWidgets.QAction(googlewindow)
        self.actionmain.setObjectName("actionmain")
        self.actionexit = QtWidgets.QAction(googlewindow)
        self.actionexit.setObjectName("actionexit")
        self.menumenus.addAction(self.actionmain)
        self.menumenus.addAction(self.actionexit)
        self.menubar.addAction(self.menumenus.menuAction())

        self.retranslateUi(googlewindow)
        QtCore.QMetaObject.connectSlotsByName(googlewindow)

    def retranslateUi(self, googlewindow):
        _translate = QtCore.QCoreApplication.translate
        googlewindow.setWindowTitle(_translate("googlewindow", "MainWindow"))
        self.pushButton.setText(_translate("googlewindow", "Search On Google!"))
        self.label_2.setText(_translate("googlewindow", "Say : Open \"Query\"!"))
        self.menumenus.setTitle(_translate("googlewindow", "menu"))
        self.actionmain.setText(_translate("googlewindow", "go to main"))
        self.actionexit.setText(_translate("googlewindow", "exit"))

