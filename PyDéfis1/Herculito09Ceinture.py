# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:13:33 2021

@author: Zacharie
"""

import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

Image = Image.open("C:/Users/Zacharie/Desktop/TD Info PT/Entrainement/PyDéfi/herculito-ex-ceinture.png")

image_array = np.array(Image)


for i in range(8//2):
    for j in range(16//2):
        if image_array[i][j][0]!=image_array[i+4][j+8][0]:
            image_array[i+4][j+8][0] = 0
        if image_array[i][j][1]!=image_array[i+4][j+8][1]:
            image_array[i+4][j+8][1] = 0
        if image_array[i][j][2]!=image_array[i+4][j+8][2]:
            image_array[i+4][j+8][2] = 0
            

plt.imshow(image_array)
plt.show()