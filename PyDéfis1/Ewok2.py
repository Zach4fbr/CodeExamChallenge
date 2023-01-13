# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:43:39 2020

@author: Zacharie
"""

fichier = open("C:\\Users\\Zacharie\\Desktop\\TD Info PT\\Entrainement\\PyDéfi\\Ewok2.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')
R = []


for i in range(len(L)):
    v = 0
    c = 0
    for x in L[i]:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == "Y":
            v += 1
        else:
            c += 1
    if c == 2*v:
        R.append(L[i])

print(len(R))