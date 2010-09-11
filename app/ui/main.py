# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Dec 31 12:56:10 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 482)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bustedButton = QtGui.QPushButton(self.centralwidget)
        self.bustedButton.setGeometry(QtCore.QRect(110, 370, 113, 32))
        self.bustedButton.setObjectName("bustedButton")
        self.plausibleButton = QtGui.QPushButton(self.centralwidget)
        self.plausibleButton.setGeometry(QtCore.QRect(260, 370, 113, 32))
        self.plausibleButton.setObjectName("plausibleButton")
        self.confirmedButton = QtGui.QPushButton(self.centralwidget)
        self.confirmedButton.setGeometry(QtCore.QRect(410, 370, 113, 32))
        self.confirmedButton.setObjectName("confirmedButton")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 80, 541, 191))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 22))
        self.menubar.setObjectName("menubar")
        self.menuQuizbusters = QtGui.QMenu(self.menubar)
        self.menuQuizbusters.setObjectName("menuQuizbusters")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit_Designer = QtGui.QAction(MainWindow)
        self.actionQuit_Designer.setObjectName("actionQuit_Designer")
        self.menuQuizbusters.addAction(self.actionQuit_Designer)
        self.menubar.addAction(self.menuQuizbusters.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Quizbusters", None, QtGui.QApplication.UnicodeUTF8))
        self.bustedButton.setText(QtGui.QApplication.translate("MainWindow", "Busted", None, QtGui.QApplication.UnicodeUTF8))
        self.plausibleButton.setText(QtGui.QApplication.translate("MainWindow", "Plausible", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmedButton.setText(QtGui.QApplication.translate("MainWindow", "Confirmed", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuizbusters.setTitle(QtGui.QApplication.translate("MainWindow", "Quizbusters", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_Designer.setText(QtGui.QApplication.translate("MainWindow", "Quit Quizbusters ", None, QtGui.QApplication.UnicodeUTF8))

