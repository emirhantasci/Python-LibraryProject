# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:51:49 2020

@author: emirh
"""


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaUI import *
from HakkindaUI import *
from girissayfasi import * 
from kayitol import * 

app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui= Ui_MainWindow() 
ui.setupUi(MainWindow)

app2=QtWidgets.QApplication(sys.argv)
MainWindow2=QtWidgets.QMainWindow()
ui2= Ui_hakkinda() 
ui2.setupUi(MainWindow2)


#giriş sayfası için bağlantılar
app3=QtWidgets.QApplication(sys.argv)
MainWindow3=QtWidgets.QMainWindow()
ui3= Ui_girispenceresi() 
ui3.setupUi(MainWindow3)

MainWindow3.show()

#kayıt sayfası için bağlantılar
app4=QtWidgets.QApplication(sys.argv)
MainWindow4=QtWidgets.QMainWindow()
ui4= Ui_kayitoll() 
ui4.setupUi(MainWindow4)

import sqlite3
global curs
global conn
conn=sqlite3.connect('veritabani.db')
curs=conn.cursor()
sorguCreTblkitaplik=("CREATE TABLE IF NOT EXISTS kitap(                         \
                     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                      \
                     Nu TEXT NOT NULL,                         \
                     Adi TEXT NOT NULL,                        \
                     YazarAdi TEXT NOT NULL,                             \
                     Yayinevi TEXT NOT NULL,                             \
                     Tarih TEXT NOT NULL,                            \
                     Tur TEXT NOT NULL,                         \
                     Raf TEXT NOT NULL,                              \
                     Ayrac TEXT NOT NULL,                             \
                     Dil TEXT NOT NULL,                            \
                     Icerik TEXT                                     )")

curs.execute(sorguCreTblkitaplik)
conn.commit()
#giriş-kayıt veritabanı bağlantısı
conn2=sqlite3.connect('GirisVeri.db') 
curs2=conn2.cursor() 
curs2.execute("CREATE TABLE IF NOT EXISTS GirisVeri (`ıd2`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,username	TEXT NOT NULL UNIQUE,passwoord	TEXT NOT NULL,adsoyad	TEXT NOT NULL)")
conn2.commit() #bağlantıyı commit ediyoruz.


def girisiac():
    MainWindow.close()
    MainWindow2.close()
    MainWindow3.show()
    MainWindow4.close()
   
def kayitiac():
    MainWindow.close()
    MainWindow2.close()
    MainWindow4.show()
    MainWindow3.close()

def hakkindaac():
    
    MainWindow4.close()
    MainWindow3.close()
    MainWindow2.show()
  
def hakkindaac():

    MainWindow2.show()
def kayitol():
    
    ad=ui4.lineEditAdSoyad.text()
    kullanici=ui4.lineEditKulAdi.text()
    sifre1=ui4.lineEditSifre.text()
    sifre2=ui4.lineEditSifreTekrar.text()
    

    if (sifre1==sifre2)and((sifre1!="")and(sifre2!="")and(kullanici!="")) :
        curs2.execute('INSERT INTO GirisVeri (username, passwoord, adsoyad ) VALUES ( ?, ?, ?)', (kullanici,sifre1,ad) )
        conn2.commit()
        ui3.statusbar.showMessage(" "*5 + " Kayıt gerçekleştirildi.", 1500)
        ui4.lineEditAdSoyad.clear() 
        ui4.lineEditKulAdi.clear()
        ui4.lineEditSifre.clear()
        ui4.lineEditSifreTekrar.clear()
        girisiac()
    else:
        ui4.statusbar.showMessage(" "*5 + " Şifreler Farklı. ", 1500)
          
    
def giris():
   
    global username
    username=ui3.lineEdit_2.text()
    passwoord=ui3.lineEdit.text()
    
    curs2.execute("SELECT * FROM GirisVeri WHERE username='%s' and passwoord='%s'" %(username,passwoord))
    conn2.commit()
    
    if(len(curs2.fetchall())>0):  
        ui.statusbar.showMessage(" "*3 + " Giriş yapıldı", 1500) 
        MainWindow3.close() 
        MainWindow.show()  
        ui3.lineEdit_2.clear()  
        ui3.lineEdit.clear()
      
        
    else:
        ui3.statusbar.showMessage(" "*3 + "Hatalı Kullanıcı Adı/Şifre", 1500)  
                    
def sifre_goster():

    if ui3.checkBox.isChecked():
        ui3.lineEdit.setEchoMode(QLineEdit.Normal)    
    else:
        ui3.lineEdit.setEchoMode(QLineEdit.Password)             


def EKLE():
    _lneNu=ui.lneNu.text()
    _lneAdi=ui.lneAdi.text()
    _lneYazarAdi=ui.lneYazarAdi.text()
    _lneYayinevi=ui.lneYayinevi.text()
    _cmbTarih=ui.cmbTarih.currentText()
    _lneTur=ui.lneTur.text()
    _spnRaf=ui.spnRaf.value()
    _cmbAyrac=ui.cmbAyrac.currentText()
    _lneDil=ui.lneDil.text()
    _lneIcerik=ui.lneIcerik.toPlainText()
            
    curs.execute("INSERT INTO kitap \
                         (Nu,Adi,YazarAdi,Yayinevi,Tarih,Tur,Raf,Ayrac,Dil,Icerik) \
                          VALUES(?,?,?,?,?,?,?,?,?,?)",\
                              (_lneNu,_lneAdi,_lneYazarAdi,_lneYayinevi,_cmbTarih,_lneTur,_spnRaf,_cmbAyrac,_lneDil,_lneIcerik,))
    
    conn.commit()
    LISTELE()
    

def LISTELE():
    
    ui.tblwBilgi.clear()
    ui.tblwBilgi.setHorizontalHeaderLabels(('No','Numara','Kitap Ad','Yazar','Yayınevi', \
                                                  'Tarih','Tür','Raf', 'Raf Ayraç', \
                                                  'Dil', 'İçerik'))
    
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    curs.execute("SELECT * FROM kitap")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tblwBilgi.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))

    ui.lneNu.clear()
    ui.lneAdi.clear()
    ui.lneYazarAdi.clear()
    ui.lneYayinevi.clear()
    ui.cmbTarih.setCurrentIndex(-1)
    ui.lneTur.clear()
    ui.spnRaf.setValue(55)
    ui.cmbAyrac.setCurrentIndex(-1)
    ui.lneDil.clear()
    ui.lneIcerik.clear()
    
    curs.execute("SELECT COUNT(*) FROM kitap")
    kayitSayisi=curs.fetchone()
    ui.lblKayitSayisi.setText(str(kayitSayisi[0]))
    
    

LISTELE()   


def CIKIS():
    cevap=QMessageBox.question(MainWindow,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(app.exec_())
    else:
        MainWindow.show()    


def SIL():
    cevap=QMessageBox.question(MainWindow,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili=ui.tblwBilgi.selectedItems()
        silinecek=secili[1].text()
        try:
            curs.execute("DELETE FROM kitap WHERE Nu='%s'" %(silinecek))
            conn.commit()
            
            LISTELE()
            
            ui.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)
            
   
def KITAPARA():
    adi=ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Adi='%s'" %(adi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row,columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No",'Numara','Kitap Adı','Yazar', \
                                                  'Yayınevi', 'Yayın Tarihi', 'Tür',  \
                                                  'Raf No', 'Raf Ayraç','Dil','İçerik'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        
        

def YAZARARA():
    YazarAdi=ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE YazarAdi='%s'" %(YazarAdi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row,columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No",'Numara','Kitap Adı','Yazar', \
                                                  'Yayınevi', 'Yayın Tarihi', 'Tür',  \
                                                  'Raf No', 'Raf Ayraç','Dil','İçerik'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)       

def YAYINEVIARA():
    yayinevi=ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Yayinevi='%s'" %(yayinevi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row,columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No",'Numara','Kitap Adı','Yazar', \
                                                  'Yayınevi', 'Yayın Tarihi', 'Tür',  \
                                                  'Raf No', 'Raf Ayraç','Dil','İçerik'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        

def TURARA():
    tur=ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Tur='%s'" %(tur))
    conn.commit()
    ui.tblwBilgi.clear()
    for row,columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No",'Numara','Kitap Adı','Yazar', \
                                                  'Yayınevi', 'Yayın Tarihi', 'Tür',  \
                                                  'Raf No', 'Raf Ayraç','Dil','İçerik'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        

def DILARA():
    dil=ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Dil='%s'" %(dil))
    conn.commit()
    ui.tblwBilgi.clear()
    for row,columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No",'Numara','Kitap Adı','Yazar', \
                                                  'Yayınevi', 'Yayın Tarihi', 'Tür',  \
                                                  'Raf No', 'Raf Ayraç','Dil','İçerik'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        
                            
def DOLDUR():
    secili=ui.tblwBilgi.selectedItems()
    ui.lneNu.setText(secili[1].text())
    ui.lneAdi.setText(secili[2].text())
    ui.lneYazarAdi.setText(secili[3].text())
    ui.lneYayinevi.setText(secili[4].text())
    ui.cmbTarih.setCurrentText(secili[5].text())
    ui.lneTur.setText(secili[6].text())
    ui.spnRaf.setValue(int(secili[7].text()))
    ui.cmbAyrac.setCurrentText(secili[8].text())
    ui.lneDil.setText(secili[9].text())
    ui.lneIcerik.setText(secili[10].text())

def GUNCELLE():
    cevap=QMessageBox.question(MainWindow,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            
            secili=ui.tblwBilgi.selectedItems()
            _Id=int(secili[0].text())
            _lneNu=ui.lneNu.text()
            _lneAdi=ui.lneAdi.text()
            _lneYazarAdi=ui.lneYazarAdi.text()
            _lneYayinevi=ui.lneYayinevi.text()
            _cmbTarih=ui.cmbTarih.currentText()
            _lneTur=ui.lneTur.text()
            _spnRaf=ui.spnRaf.value()
            _cmbAyrac=ui.cmbAyrac.currentText()
            _lneDil=ui.lneDil.text()
            _lneIcerik=ui.lneIcerik.toPlainText()
        
                       
            curs.execute("UPDATE kitap SET Nu=?, Adi=?, YazarAdi=?, Yayinevi=?, Tarih=?, Tur=?, Raf=?, Ayrac=?, Dil=?, Icerik=? WHERE Id=?", \
                         (_lneNu,_lneAdi,_lneYazarAdi,_lneYayinevi,_cmbTarih,_lneTur,_spnRaf,_cmbAyrac,_lneDil,_lneIcerik,_Id))
            conn.commit()
            
            LISTELE()
            
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncellme iptal edildi",10000)
            
def HAKKINDA():
    MainWindow2.show()
    
    
    
    
    
def ANACIKIS():
    cevap=QMessageBox.question(MainWindow,"ÇIKIŞ","Kütüphane sisteminden ayrılmak istediğinize emin misiniz?", \
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(app.exec_())
    else:
        MainWindow3.show()
        
        
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAd.clicked.connect(KITAPARA)
ui.btnYazar.clicked.connect(YAZARARA)
ui.btnYayinEvi.clicked.connect(YAYINEVIARA)
ui.btnDil.clicked.connect(DILARA)
ui.btnTur.clicked.connect(TURARA)
ui.tblwBilgi.itemSelectionChanged.connect(DOLDUR)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.menuHakkinda.triggered.connect(HAKKINDA)
ui3.pushButton_2.clicked.connect(kayitiac)    
ui3.pushButton.clicked.connect(giris)    
ui3.checkBox.clicked.connect(sifre_goster)
ui3.actionKay_t_Ol.triggered.connect(kayitiac)
ui3.action_k.triggered.connect(ANACIKIS)
ui3.actionHakk_nda.triggered.connect(HAKKINDA)
ui4.giris.clicked.connect(girisiac)
ui4.kayitol.clicked.connect(kayitol) 

sys.exit(app.exec_())
