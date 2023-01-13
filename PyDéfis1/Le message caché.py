# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:47:09 2021

@author: Zacharie
"""


import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt



img = mpimg.imread('C:/Users/Zacharie/Desktop/PyDéfi/cocotiers_s2.png')

if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
    
R = np.copy(img) # On fait une copie de l'original
B = []
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        r, v, b = img[i, j]
        R[i, j] = (r, v, b)
        r = int(bin(r)[-1])
        v = int(bin(v)[-1])
        b = int(bin(b)[-1])
        B.append([r,v,b])
        
plt.imshow(R)
plt.show()

ch = ""
for i in range(len(B)):
    for j in range(len(B[i])):
        ch += str(B[i][j])

message = ""
lg = len(ch)//8
for i in range(lg):
    bit = ch[8*i:8*(i+1)]
    asc = int(bit,2)
    message += chr(asc)
        
