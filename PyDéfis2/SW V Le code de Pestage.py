# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:57:33 2022

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/SW V Le code de Pestage 2.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split('\n')

P11 = []
P12 = []
P21 = []
P22 = []
for i in range(0,len(L)-1,2):
    p11 = ""
    p12 = ""
    p21 = ""
    p22 = ""
    for j in range(0,len(L[i])-1,2):
        p11 += L[i][j]
        p12 += L[i][j+1]   
        p21 += L[i+1][j]
        p22 += L[i+1][j+1]
    P11.append(p11)
    P12.append(p12)
    P21.append(p21)
    P22.append(p22)
    
#Boba Fett
#Maître Yoda
#Dark Vador
#BB8