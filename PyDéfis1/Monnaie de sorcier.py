# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:29:28 2021

@author: Zacharie
"""

def chiffres(char):
    S = []
    for x in char:
        a = x in S
        if a == False:
            S.append(x)
    return sorted(S)
    

G = []
for g in range(1000000): #gallions
    m = 17*g            #mornilles
    n = 29*m            #noises
    g = str(g)
    m = str(m)
    n = str(n)
    if chiffres(g)==chiffres(m) and chiffres(g)==chiffres(n):
        G.append(g)
    g,m,n = int(g),int(m),int(n)
        
    
    