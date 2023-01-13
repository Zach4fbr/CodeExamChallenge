# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:53:59 2021

@author: Zacharie
"""

#from itertools import combinations
from itertools import combinations_with_replacement

L = [1, 2, 3, 7, 10, 20, 25]
#tot = 10
tot = 26


comb = []
for n in range(1,30):
    comb.append([i for i in combinations_with_replacement(L,n)])
    
    
R = []
for i in range(len(comb)):
    for j in range(len(comb[i])):
        s = sum(comb[i][j])
        if s == tot:
            R.append(comb[i][j])
            
print(len(R))