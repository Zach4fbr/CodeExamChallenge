# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:56:13 2021

@author: Zacharie
"""

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img = mpimg.imread('C:/Users/Zacharie/Desktop/PyDéfi/IUT_RT_STEG.png')
if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)



def codage(r,v,b,a):
    if a == 255:
        return ""
    if a == 254:
        return bin(b)[-1]
    if a == 253:
        return bin(v)[-1]
    if a == 252:
        return bin(r)[-1]
    if a == 251:
        return bin(b)[-1]+bin(v)[-1]
    if a == 250:
        return bin(b)[-1]+bin(r)[-1]
    if a == 249:
        return bin(v)[-1]+bin(b)[-1]
    if a == 248:
        return bin(v)[-1]+bin(r)[-1]
    if a == 247:
        return bin(r)[-1]+bin(b)[-1]
    if a == 246:
        return bin(r)[-1]+bin(v)[-1]
    if a == 245:
        return bin(b)[-1]+bin(v)[-1]+bin(r)[-1]
    if a == 244:
        return bin(b)[-1]+bin(r)[-1]+bin(v)[-1]
    if a == 243:
        return bin(v)[-1]+bin(b)[-1]+bin(r)[-1]
    if a == 242:
        return bin(v)[-1]+bin(r)[-1]+bin(b)[-1]
    if a == 241:
        return bin(r)[-1]+bin(b)[-1]+bin(v)[-1]
    if a == 240:
        return bin(r)[-1]+bin(v)[-1]+bin(b)[-1]
    else:
        return ""

   
R = np.copy(img) # On fait une copie de l'original
ch = ""
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        r, v, b, a = img[i, j] #rouge,vert,bleu,alpha : transparence
        ch += codage(r,v,b,a)
        
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


print(decode_binary_string(ch))

