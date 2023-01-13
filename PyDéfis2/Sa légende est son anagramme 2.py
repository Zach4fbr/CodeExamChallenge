# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:44:58 2021

@author: Zacharie
"""

from collections import Counter

fichier = open("C:/Users/Zacharie/Desktop/TD Info PT/Entrainement/PyDéfi/Sa légende est son anagramme 2.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')
for i in range(len(L)):
    L[i] = L[i].lower()
    L[i] = L[i].replace('ã«','e')
    L[i] = L[i].replace('ã©','e')
    L[i] = L[i].replace('ã¯','i')
    L[i] = L[i].replace('ã‰','e')
    L[i] = L[i].replace('ã¨','e')

A = []
M = 0
s = 0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if Counter(L[i])==Counter(L[j]):
            s += 1
            if s > M:
                M = s
                A.append([L[i],L[j]])
            
#['elia marchand', 'dina marechal']
#['elia marchand', 'charline adam']
#['elia marchand', 'diane marchal']

