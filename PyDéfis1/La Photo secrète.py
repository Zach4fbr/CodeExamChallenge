# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:46:21 2021

@author: Zacharie
"""

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


img = mpimg.imread('C:/Users/Zacharie/Desktop/PyDéfi/poke_crypto_cle1.png')
img2 = mpimg.imread('C:/Users/Zacharie/Desktop/PyDéfi/poke_crypto_cle2.png')

if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
if img2.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img2 = (img2 * 255).astype(np.uint8)

R = np.copy(img) # On fait une copie de l'original
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        r, v, b = img[i, j]
        r2, v2, b2 = img2[i, j]
        if r == r2:
                 couleur = v ^ v2
                 R[i, j] = (couleur, couleur, couleur)
        else:
            couleur = b ^ b2
            R[i,j] = (couleur, couleur, couleur)

plt.imshow(R)
plt.show()