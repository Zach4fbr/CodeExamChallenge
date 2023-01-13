# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:13:11 2021

@author: Zacharie
"""

import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

Image = Image.open("C:/Users/Zacharie/Desktop/PyDéfi/portrait.png")
image_array = np.array(Image)

T = np.copy(image_array)

def modif(L):
    a = bin(L[0])[2:]
    ta = len(a)
    a = (8-ta)*'0'+a
    a = a[::-1]
    b = bin(L[1])[2:]
    tb = len(b)
    b = (8-tb)*'0'+b
    b = b[::-1]
    c = bin(L[2])[2:]
    tc = len(c)
    c = (8-tc)*'0'+c
    c = c[::-1]
    a = bin2dec(a)
    b = bin2dec(b)
    c = bin2dec(c)
    return [a,b,c]

def bin2dec(ch):
    s = 0
    n = len(ch)
    for i in range(n):
        s += int(ch[i])*2**(n-i-1)
    return s
           



(largeur, hauteur)= Image.size
for x in range(largeur):
    for y in range(hauteur):
        # Ici on traite le pixel (x,y) de l'image i.
        (rouge,vert,bleu) = Image.getpixel((x,y))
        (rouge,vert,bleu) = modif([rouge,vert,bleu])
        Image.putpixel((x,y),(rouge,vert,bleu))
        

plt.imshow(Image)
plt.show()
