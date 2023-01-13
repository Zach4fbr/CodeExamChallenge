# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:43:23 2021

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/Matrix.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')

def ascii2nb(caractere):
    if caractere != " ":
        code = ord(caractere)
        return code
    else:
        return 0

s = 0
for i in range(len(L)):
    for j in range(len(L[i])):
        s += (i+1)*(j+1)*ascii2nb(L[i][j])

print("empreinte = ",s)
