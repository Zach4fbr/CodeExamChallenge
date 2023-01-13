# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:26:10 2020

@author: Zacharie
"""

S = []
s = 0
for h in range(0,20+1):
    for k in range(0,100000+1):
        S.append((8*k+7)*4**h) #Théorème énoncé par Fermat 
        
for i in range(len(S)):
    if S[i] <= 10000:
        s += 1
print(s)