# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:35:12 2020

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/TD Info PT/Entrainement/PyDéfi/Le plus rare de tous.txt")
ligne = fichier.readlines()
fichier.close()

S = []
N = []

def nbpokemon(chc,L):
    n = 0
    for i in range(len(L)):
        if L[i] == chc:
            n += 1
    return n

for i in range(len(ligne)):
    S.append(ligne[i].split(','))
    N.append(S[i][0])


for i in range(len(N)):
    n = nbpokemon(N[i],N)
    if n == 3:
        print(N[i],i)