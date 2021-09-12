#----------------------
# -*- coding: utf-8 -*-
#----------------------
import os
# install: pip install --upgrade arabic-reshaper
import arabic_reshaper
# install: pip install python-bidi
from bidi.algorithm import get_display
#-------------------------------
os.system("chcp 1256 & cls")
#-------------------------------
txt = get_display(arabic_reshaper.reshape("سلام ایران"))
print(txt)
#------------------------------
txt2 = get_display(arabic_reshaper.reshape("این متن برای تست متن فارسی است"))
print(txt2)
#------------------------------
txt3 = get_display(arabic_reshaper.reshape("متن به صورت کامل در ترمینال پرینت می شود."))
print(txt3)
