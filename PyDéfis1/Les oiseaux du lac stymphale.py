# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:57:59 2021

@author: Zacharie
"""

import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

Image = Image.open("C:/Users/Zacharie/Desktop/PyDéfi/lake.png")
image_array = np.array(Image)

plt.imshow(Image)
plt.show()

s = 0

for i in range(250):
    for j in range(500):
        s += image_array[i][j]
        
print(s)