# -*- coding: cp1252 -*-
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from libmicrocontest2_python27 import *

cont = commence_contest(56, "Zach4", " 
 
img_data = cont.get_str("img_b64")

#img_data = b'iVBORw0KGgoAAAANSUhEUgAAANgAAADVAQMAAAAPcKxwAAAAA1BMVEXIARLSZLorAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAHUlEQVRYhe3BgQAAAADDoPlT3+AEVQEAAAAAAM8AF0wAAbKmtdoAAAAASUVORK5CYII='

# In Python 2.7
fh = open("imageToSave.png", "wb")
fh.write(img_data.decode('base64'))
fh.close()

img = mpimg.imread('C:/Users/Zacharie/Desktop/�Contest/imageToSave.png')


if img.dtype == np.float32: # Si le r�sultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
    
R = np.copy(img) # On fait une copie de l'original
r = R[0][0][0]
g = R[0][0][1]
b = R[0][0][2]
print(r,g,b)
cont.append_answer("r", r)
cont.append_answer("g", g)
cont.append_answer("b", b)
print(cont.submit_answer())
