# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:48:10 2021

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/Un message bien enfoui.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')

def str_2_nb(car):
    for x in "0123456789":
        if car==x:
            return int(car)
    return 0

S = []
C = []
for i in range(len(L)):
    s1 = 0
    s2 = 0
    c1 = L[i].split(" ")
    C.append(c1)
    for j in range(len(C[i][0])):
        s1 += str_2_nb(C[i][0][j]) 
    for j in range(len(C[i][1])):
        s2 += str_2_nb(C[i][1][j])
    S.append([s1,s2])

D = []
for i in range(len(S)):
    if S[i][0]%13==0 and S[i][1]%13==0:
        D.append(L[i])
        
rep = "RENDEZVOUS15h57"