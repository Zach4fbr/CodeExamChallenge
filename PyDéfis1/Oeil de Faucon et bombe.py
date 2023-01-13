# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:18:13 2020

@author: Zacharie
"""

n = 5000

L1 = [i for i in range(1,n+1)]
L2 = []
L3 = []
L4 = []
L5 = []

for i in range(1,n+1):
    if i % 5 == 0:
        L2.append(i)
    else :
        if i % 7 == 0:
            L2.append(i)

for i in range(len(L2)):
    #à gauche, les dizaines et à droite, les unités
    if (L2[i]//10 - 10*(L2[i]//100)) <= (L2[i] - 10*(L2[i]//10)): 
        L3.append(L2[i])
        
for i in range(len(L3)-1):
    #unité
    if L3[i+1] - 10*(L3[i+1]//10) < 5:
        L4.append(L3[i])
    
for i in range(len(L4)):
    #dizaine
    if (L4[i]//10 - 10*(L4[i]//100)) % 2 == 1:
        L5.append(L4[i])
        
print(L5[24],L5[25])
    
