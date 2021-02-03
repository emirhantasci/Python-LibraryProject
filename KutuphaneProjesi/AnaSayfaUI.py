# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 779)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Sulu-boya-kitap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 0, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 686, 291, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lblKayitSayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblKayitSayisi.setGeometry(QtCore.QRect(330, 680, 61, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblKayitSayisi.setFont(font)
        self.lblKayitSayisi.setText("")
        self.lblKayitSayisi.setObjectName("lblKayitSayisi")
        self.tblwBilgi = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwBilgi.setGeometry(QtCore.QRect(10, 380, 941, 291))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.tblwBilgi.setFont(font)
        self.tblwBilgi.setRowCount(100)
        self.tblwBilgi.setColumnCount(11)
        self.tblwBilgi.setObjectName("tblwBilgi")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 3, 271, 301))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lneNu = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneNu.setFont(font)
        self.lneNu.setObjectName("lneNu")
        self.horizontalLayout.addWidget(self.lneNu)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lneAdi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneAdi.setFont(font)
        self.lneAdi.setObjectName("lneAdi")
        self.horizontalLayout_2.addWidget(self.lneAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lneYazarAdi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneYazarAdi.setFont(font)
        self.lneYazarAdi.setObjectName("lneYazarAdi")
        self.horizontalLayout_3.addWidget(self.lneYazarAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lneYayinevi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneYayinevi.setFont(font)
        self.lneYayinevi.setObjectName("lneYayinevi")
        self.horizontalLayout_4.addWidget(self.lneYayinevi)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.cmbTarih = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.cmbTarih.setFont(font)
        self.cmbTarih.setObjectName("cmbTarih")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.cmbTarih.addItem("")
        self.horizontalLayout_5.addWidget(self.cmbTarih)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lneTur = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneTur.setFont(font)
        self.lneTur.setObjectName("lneTur")
        self.horizontalLayout_6.addWidget(self.lneTur)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.btnCikis = QtWidgets.QPushButton(self.centralwidget)
        self.btnCikis.setGeometry(QtCore.QRect(857, 680, 91, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCikis.setFont(font)
        self.btnCikis.setObjectName("btnCikis")
        self.lneIcerik = QtWidgets.QTextEdit(self.centralwidget)
        self.lneIcerik.setGeometry(QtCore.QRect(310, 30, 631, 131))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneIcerik.setFont(font)
        self.lneIcerik.setObjectName("lneIcerik")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 170, 291, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spnRaf = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.spnRaf.setFont(font)
        self.spnRaf.setObjectName("spnRaf")
        self.verticalLayout_3.addWidget(self.spnRaf)
        self.cmbAyrac = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.cmbAyrac.setFont(font)
        self.cmbAyrac.setObjectName("cmbAyrac")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.cmbAyrac.addItem("")
        self.verticalLayout_3.addWidget(self.cmbAyrac)
        self.lneDil = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneDil.setFont(font)
        self.lneDil.setObjectName("lneDil")
        self.verticalLayout_3.addWidget(self.lneDil)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 340, 931, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.lneAra = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lneAra.setFont(font)
        self.lneAra.setObjectName("lneAra")
        self.horizontalLayout_8.addWidget(self.lneAra)
        self.btnAd = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnAd.setFont(font)
        self.btnAd.setObjectName("btnAd")
        self.horizontalLayout_8.addWidget(self.btnAd)
        self.btnYazar = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnYazar.setFont(font)
        self.btnYazar.setObjectName("btnYazar")
        self.horizontalLayout_8.addWidget(self.btnYazar)
        self.btnYayinEvi = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnYayinEvi.setFont(font)
        self.btnYayinEvi.setObjectName("btnYayinEvi")
        self.horizontalLayout_8.addWidget(self.btnYayinEvi)
        self.btnTur = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnTur.setFont(font)
        self.btnTur.setObjectName("btnTur")
        self.horizontalLayout_8.addWidget(self.btnTur)
        self.btnDil = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnDil.setFont(font)
        self.btnDil.setObjectName("btnDil")
        self.horizontalLayout_8.addWidget(self.btnDil)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnListele.setFont(font)
        self.btnListele.setObjectName("btnListele")
        self.horizontalLayout_8.addWidget(self.btnListele)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(620, 170, 321, 141))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSil.setFont(font)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_4.addWidget(self.btnSil)
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnEkle.setFont(font)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_4.addWidget(self.btnEkle)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnGuncelle.setFont(font)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_4.addWidget(self.btnGuncelle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 26))
        self.menubar.setObjectName("menubar")
        self.menuYARIDM = QtWidgets.QMenu(self.menubar)
        self.menuYARIDM.setObjectName("menuYARIDM")
        MainWindow.setMenuBar(self.menubar)
        self.actionHAKKINDA = QtWidgets.QAction(MainWindow)
        self.actionHAKKINDA.setObjectName("actionHAKKINDA")
        self.menuHakkinda = QtWidgets.QAction(MainWindow)
        self.menuHakkinda.setObjectName("menuHakkinda")
        self.menuYARIDM.addAction(self.menuHakkinda)
        self.menubar.addAction(self.menuYARIDM.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kütüphane"))
        self.label_7.setText(_translate("MainWindow", "İçerik:"))
        self.label_11.setText(_translate("MainWindow", "Veri Tabanında Kayıtlı Kitap Sayısı:"))
        self.label.setText(_translate("MainWindow", "Kitap No:"))
        self.label_2.setText(_translate("MainWindow", "Kitap Adı:"))
        self.label_3.setText(_translate("MainWindow", "Yazar Adı:"))
        self.label_4.setText(_translate("MainWindow", "Yayınevi:"))
        self.label_5.setText(_translate("MainWindow", "Yayın Tarihi:"))
        self.cmbTarih.setItemText(0, _translate("MainWindow", "2020"))
        self.cmbTarih.setItemText(1, _translate("MainWindow", "2019"))
        self.cmbTarih.setItemText(2, _translate("MainWindow", "2018"))
        self.cmbTarih.setItemText(3, _translate("MainWindow", "2017"))
        self.cmbTarih.setItemText(4, _translate("MainWindow", "2016"))
        self.cmbTarih.setItemText(5, _translate("MainWindow", "2015"))
        self.cmbTarih.setItemText(6, _translate("MainWindow", "2014"))
        self.cmbTarih.setItemText(7, _translate("MainWindow", "2013"))
        self.cmbTarih.setItemText(8, _translate("MainWindow", "2012"))
        self.cmbTarih.setItemText(9, _translate("MainWindow", "2011"))
        self.cmbTarih.setItemText(10, _translate("MainWindow", "2010"))
        self.cmbTarih.setItemText(11, _translate("MainWindow", "2009"))
        self.cmbTarih.setItemText(12, _translate("MainWindow", "2008"))
        self.cmbTarih.setItemText(13, _translate("MainWindow", "2007"))
        self.cmbTarih.setItemText(14, _translate("MainWindow", "2006"))
        self.cmbTarih.setItemText(15, _translate("MainWindow", "2005"))
        self.cmbTarih.setItemText(16, _translate("MainWindow", "2004"))
        self.cmbTarih.setItemText(17, _translate("MainWindow", "2003"))
        self.cmbTarih.setItemText(18, _translate("MainWindow", "2002"))
        self.cmbTarih.setItemText(19, _translate("MainWindow", "2001"))
        self.cmbTarih.setItemText(20, _translate("MainWindow", "2000"))
        self.cmbTarih.setItemText(21, _translate("MainWindow", "1999"))
        self.cmbTarih.setItemText(22, _translate("MainWindow", "1998"))
        self.label_6.setText(_translate("MainWindow", "Tür:"))
        self.btnCikis.setText(_translate("MainWindow", "Çıkış"))
        self.label_8.setText(_translate("MainWindow", "Raf No:"))
        self.label_9.setText(_translate("MainWindow", "Raf Ayraç:"))
        self.label_10.setText(_translate("MainWindow", "Dil:"))
        self.cmbAyrac.setItemText(0, _translate("MainWindow", "A"))
        self.cmbAyrac.setItemText(1, _translate("MainWindow", "B"))
        self.cmbAyrac.setItemText(2, _translate("MainWindow", "C"))
        self.cmbAyrac.setItemText(3, _translate("MainWindow", "D"))
        self.cmbAyrac.setItemText(4, _translate("MainWindow", "E"))
        self.cmbAyrac.setItemText(5, _translate("MainWindow", "F"))
        self.cmbAyrac.setItemText(6, _translate("MainWindow", "G"))
        self.cmbAyrac.setItemText(7, _translate("MainWindow", "H"))
        self.cmbAyrac.setItemText(8, _translate("MainWindow", "I"))
        self.cmbAyrac.setItemText(9, _translate("MainWindow", "J"))
        self.cmbAyrac.setItemText(10, _translate("MainWindow", "K"))
        self.cmbAyrac.setItemText(11, _translate("MainWindow", "L"))
        self.cmbAyrac.setItemText(12, _translate("MainWindow", "M"))
        self.cmbAyrac.setItemText(13, _translate("MainWindow", "N"))
        self.cmbAyrac.setItemText(14, _translate("MainWindow", "O"))
        self.cmbAyrac.setItemText(15, _translate("MainWindow", "P"))
        self.cmbAyrac.setItemText(16, _translate("MainWindow", "R"))
        self.cmbAyrac.setItemText(17, _translate("MainWindow", "S"))
        self.cmbAyrac.setItemText(18, _translate("MainWindow", "T"))
        self.cmbAyrac.setItemText(19, _translate("MainWindow", "U"))
        self.cmbAyrac.setItemText(20, _translate("MainWindow", "V"))
        self.cmbAyrac.setItemText(21, _translate("MainWindow", "Y"))
        self.cmbAyrac.setItemText(22, _translate("MainWindow", "Z"))
        self.label_15.setText(_translate("MainWindow", "Aranacak Kelime:"))
        self.btnAd.setText(_translate("MainWindow", "Kitap Adı"))
        self.btnYazar.setText(_translate("MainWindow", "Yazar Adı"))
        self.btnYayinEvi.setText(_translate("MainWindow", "Yayınevi"))
        self.btnTur.setText(_translate("MainWindow", "Tür"))
        self.btnDil.setText(_translate("MainWindow", "Dil"))
        self.btnListele.setText(_translate("MainWindow", "Tüm Kaydı Listele"))
        self.btnSil.setText(_translate("MainWindow", "Kaydı Sil"))
        self.btnEkle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.btnGuncelle.setText(_translate("MainWindow", "Kayıt Güncelle"))
        self.menuYARIDM.setTitle(_translate("MainWindow", "Diğer"))
        self.actionHAKKINDA.setText(_translate("MainWindow", "HAKKINDA"))
        self.menuHakkinda.setText(_translate("MainWindow", "Hakkında"))

