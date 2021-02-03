# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:10:26 2020

@author: emirh
"""

from PyQt5 import uic

with open('AnaSayfaUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('AnaSayfa.ui', fout)



with open('HakkindaUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('Hakkinda.ui', fout)



with open('girissayfasi.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('girissayfasi.ui', fout)



with open('kayitol.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('kayitol.ui', fout)
