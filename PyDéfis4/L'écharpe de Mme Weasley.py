# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:37:40 2022

@author: Zacharie
"""

import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

Image = Image.open("C:/Users/Zacharie/Desktop/PyDéfi/message_echarpe_exemple.png")
image_array = np.array(Image)
         
N = [[],[],[],[]]


(largeur, hauteur)= Image.size
for x in range(largeur):
    for y in range(hauteur):
        # Ici on traite le pixel (x,y) de l'image i.
        (rouge,vert,bleu) = Image.getpixel((x,y))
        if y <= 7:
            N[0].append((rouge,vert,bleu))
        if y>7 and y<=15:
            N[1].append((rouge,vert,bleu))
        if y>15 and y<=23:
            N[2].append((rouge,vert,bleu))
        if y>23:
            N[3].append((rouge,vert,bleu))
            
#il y a dans N2 les 4 lignes 


plt.imshow(Image)
plt.show()
