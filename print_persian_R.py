#----------------------
# -*- coding: utf-8 -*-
#----------------------
import os,shutil
# install: pip install --upgrade arabic-reshaper
import arabic_reshaper
# install: pip install python-bidi
from bidi.algorithm import get_display 
#-------------------------------
os.system("chcp 1256 & cls")
#-------------------------------
def farsi_print(txt):
    columns=shutil.get_terminal_size((80, 20)).columns
    txt2=[]
    txt3=''
    for n in txt:
        if n!="\n":
            txt3+=n
        else:
            txt2.append(txt3)
            txt3=''
    txt2.append(txt3)
    txt3=''
    for line in txt2:
        reshaped_text = arabic_reshaper.reshape(line)
        bidi_text = get_display(reshaped_text)
        bidi_text = bidi_text.rjust(columns-1)
        return(bidi_text)
#-------------------------------
txt0 = farsi_print("سلام ایران")
print(txt0)
#------------------------------
txt2 = farsi_print("این متن برای تست متن فارسی است")
print(txt2)
#------------------------------
txt3 = farsi_print("متن به صورت کامل در ترمینال پرینت می شود.")
print(txt3)
