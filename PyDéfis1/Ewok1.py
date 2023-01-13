# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:42:43 2020

@author: Zacharie
"""

fichier = open("C:\\Users\\Zacharie\\Desktop\\TD Info PT\\Entrainement\\PyDéfi\\Ewok1.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')
R = []

def recherche(car,a):
    for x in car:
        if x == str(a):
            return True
    return False
        
for i in range(len(L)):
    if recherche(L[i],'a') == False and recherche(L[i],'A') == False:
        R.append(L[i])

R.pop()
print(len(R))



