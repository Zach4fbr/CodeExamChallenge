# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:45:58 2020

@author: Zacharie
"""

fichier = open("C:\\Users\\Zacharie\\Desktop\\TD Info PT\\Entrainement\\PyDéfi\\Le lion de Némée.txt",'r')
ligne = fichier.read()
fichier.close()

l = ligne.split('\n')
r = []

A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26

s = 0
a = []
b = []

for i in range(len(l)):
    for x in l[i]:
        s += eval(x)
    a.append(s)
    b.append(l[i])
    
#sorted(a)



