# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:05:40 2022

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/Hen Llinge obfusqué.txt","r")
ligne = fichier.readlines()
fichier.close()

t = ligne[0]
x = ligne[2]

def transfo(ch):
    aA = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    Aa = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    rep = ""
    i = 0
    while i<len(ch)-1:
        s = ch[i]+ch[i+1]
        if s in aA or s in Aa:
            i += 2
            rep += ""
        else:
            rep += ch[i]
            i += 1
    rep += ch[-1]
    return rep

for i in range(10):
    x = transfo(x)
    
print(x)