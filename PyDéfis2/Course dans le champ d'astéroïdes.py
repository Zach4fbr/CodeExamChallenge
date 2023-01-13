# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:22:06 2020

@author: Zacharie
"""

import numpy as np
from collections import OrderedDict

fichier = open("C:\\Users\\Zacharie\\Desktop\\PyDéfi\\Course dans le champ d'astéroïdes.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')
N = []  #nom astéroïdes
O = []  #nom Obi-Wan
C = []

for i in range(len(L)-11):
    N.append(L[i])
    C.append(L[i][12:].split(','))
for i in range(len(L)-10,len(L)):
    O.append(L[i].split(','))
for i in range(len(O)):
    for j in range(len(O[i])):
            O[i][j] = float(O[i][j])
for i in range(len(C)):
    for j in range(len(C[i])):
            C[i][j] = float(C[i][j])

def Vect(point1,point2):
    x1,y1,z1 = point1[0],point1[1],point1[2]
    x2,y2,z2 = point2[0],point2[1],point2[2]
    return (x2-x1,y2-y1,z2-z1)

def Norme(point):
    x,y,z = point[0],point[1],point[2]
    return np.sqrt(x**2+y**2+z**2)
    
def DistPointDroite(A,B,H):
    BH = Vect(H,B)
    BA = Vect(A,B)
    BD = np.cross(BH,BA)
    HA = Vect(A,H)
    if Norme(BD)>Norme(BA):
        return min(Norme(BH),Norme(HA))
    return Norme(np.cross(BH,BA))/Norme(BA)
    
R = []
for i in range(len(O)-1):
    for j in range(len(C)):
        d = DistPointDroite(O[i],O[i+1],C[j])
        R.append((d,N[j]))
R2 = []
for i in range(len(R)):
    R2.append(sorted(R)[i][1][:9])

R3 = list(OrderedDict.fromkeys(R2))

print(R3[:9])
    