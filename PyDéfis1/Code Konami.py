# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:59:35 2022

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/Code Konami.txt",'r', encoding="utf-8")
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')

L2 = []

for i in range(36):
    L2.append(L[i].split(" -> "))
    
def correspond(L,ch):
    for i in range(len(L)):
        if L[i][0] == ch:
            return L[i][1]
    return False

t = ""
for i in range(37,59):
    t += L[i]

R = ""
for i in range(0,len(t)-1,2):
    ch = t[i]+t[i+1]
    R += correspond(L2,ch)