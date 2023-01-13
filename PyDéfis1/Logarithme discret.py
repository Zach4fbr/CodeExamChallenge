# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:06:04 2021

@author: Zacharie
"""

L = [50, 36, 153, 128, 71, 23, 75, 55, 208, 121]


def recherche(el,L):
    for i in range(len(L)):
        if el == L[i]:
            return i
    return False

N = []
for i in range(len(L)):
    
    r = []
    for x in range(1,1000):
        r.append((3**x)%223)
    
    N.append(recherche(L[i],r)+1)


print(N)