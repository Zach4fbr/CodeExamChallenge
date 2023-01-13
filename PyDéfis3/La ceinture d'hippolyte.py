# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:29:13 2021

@author: Zacharie
"""

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt



img = mpimg.imread('C:/Users/Zacharie/Desktop/PyDéfi/herculito-ceinture.png')

if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
    
R = np.copy(img) # On fait une copie de l'original
B = []
for i in range(R.shape[0]):
    for j in range(R.shape[1]//2):
        r, v, b = img[i, j]
        r2,v2,b2 = img[i, j+R.shape[1]//2]
        if r!=r2 or v!=v2 or b!=b2:
            R[i,j+R.shape[1]//2] = [0,0,0]
        
plt.imshow(R)
plt.show()

#plus lisible avec IDLE