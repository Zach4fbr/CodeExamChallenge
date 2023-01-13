import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

folder = "C:/Users/Zacharie/Desktop/PyDéfi/"
filename = "maraudeur.png"

img = imread(folder+filename)
carte = np.zeros_like(img)

rshape, cshape = img.shape[:2]
n = rshape * cshape
a, b = 53911, 15677

for row in range(rshape):
    for col in range(cshape):
        i = row*cshape + col
        j = (a*i+b)%n
        row2 = j//cshape
        col2 = j%cshape
        carte[row,col] = img[row2,col2]

plt.imshow(carte[800:1200,:500,:])