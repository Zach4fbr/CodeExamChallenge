# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:45:56 2021

@author: Zacharie
"""

from itertools import combinations

#L = [3,6,4,5,1]
#tot = 8
L = [32, 37, 41, 42, 45, 49, 50, 51, 17, 54, 55, 28, 62]
tot = 249



comb = []
for n in range(2,len(L)+1):
    comb.append([i for i in combinations(L,n)])
    
    
R = []
for i in range(len(comb)):
    for j in range(len(comb[i])):
        s = sum(comb[i][j])
        if s <= tot:
            R.append(comb[i][j])
            
print(len(R))