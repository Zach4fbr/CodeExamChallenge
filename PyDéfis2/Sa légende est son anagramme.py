# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:09:10 2020

@author: Zacharie
"""

from collections import Counter

fichier = open("C:\\Users\\Zacharie\\Desktop\\TD Info PT\\Entrainement\\PyDéfi\\Sa légende est son anagramme.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')
for i in range(len(L)):
    L[i] = L[i].lower()
    L[i] = L[i].replace('ã«','e')
    L[i] = L[i].replace('ã©','e')

A = []

#Pierre Maréchal
t = "pierre marechal"

for i in range(len(L)):
    if Counter(L[i]) == Counter(t):
        A.append(L[i])
print(A)