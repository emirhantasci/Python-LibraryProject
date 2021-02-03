# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hakkinda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hakkinda(object):
    def setupUi(self, hakkinda):
        hakkinda.setObjectName("hakkinda")
        hakkinda.resize(520, 206)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Sulu-boya-kitap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hakkinda.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(hakkinda)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        hakkinda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hakkinda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 26))
        self.menubar.setObjectName("menubar")
        hakkinda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hakkinda)
        self.statusbar.setObjectName("statusbar")
        hakkinda.setStatusBar(self.statusbar)

        self.retranslateUi(hakkinda)
        QtCore.QMetaObject.connectSlotsByName(hakkinda)

    def retranslateUi(self, hakkinda):
        _translate = QtCore.QCoreApplication.translate
        hakkinda.setWindowTitle(_translate("hakkinda", "Kütüphane - Hakkında"))
        self.label.setText(_translate("hakkinda", "Emirhan Taşçı tarafından yapılmıştır. "))
        self.label_2.setText(_translate("hakkinda", "instagram.com/TeknoBol"))

