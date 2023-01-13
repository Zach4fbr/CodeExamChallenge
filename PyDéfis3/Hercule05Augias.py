# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:20:18 2021

@author: Zacharie
"""

import numpy
import matplotlib.pyplot as plt

image = plt.imread("C:/Users/Zacharie/Desktop/PyDéfi/stables.png")

def coloriage_pixel_pile(image,result,shape,seuil,valeur,pile,i,j):
    image[j][i] = valeur
    result[j][i] = 255
    voisins = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
    for pixel in voisins:
        (k,l) = pixel
        if k>=0 and k<shape[1] and l>=0 and l<shape[0]:
            if image[l][k]>seuil:
                image[l][k] = valeur
                pile.append(pixel)

def analyse(image,seuil):
    shape = image.shape
    Nx = shape[1]
    Ny = shape[0]
    compteur = 0
    positions = []
    result = numpy.zeros((Ny,Nx),dtype=numpy.uint8)
    for y in range(Ny):
        for x in range(Nx):
            if image[y][x] > seuil:
                compteur += 1
                pile = [(x,y)]
                si = 0
                sj = 0
                npix = 0
                while len(pile)>0:
                    (i,j) = pile.pop()
                    si += i
                    sj += j
                    npix += 1
                    coloriage_pixel_pile(image,result,shape,seuil,0,pile,i,j)
                xb = si*1.0/npix
                yb = sj*1.0/npix
                positions.append((xb,yb,npix))
    print("Nombre de taches : %d"%compteur)
    for p in positions:
        print("x=%f, y=%f, npix=%d"%(p[0],p[1],p[2]))
    return (positions,result,compteur)

print("L'image a :",analyse(image,0)[2], "régions")

