# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:01:24 2022

@author: Zacharie
"""

from itertools import product

L = ["A","T","C","G"]

comb = [i for i in product('ATCG',repeat=6)]
for n in range(len(comb)):
    s = ""
    for x in comb[n]:
       s+=x
    comb[n]=s

def norn(adn1,adn2):
    s = 0
    for i in range(len(adn1)):
        if adn1[i] != adn2[i]:
            s += 1
    return s

def nb(adn1):
    R = [adn1]
    for i in range(len(comb)):
        s = 0
        for j in range(len(R)):
            adn2 = comb[i]
            adn1 = R[j]
            if norn(adn1,adn2) >= 3:
                s += 1
                if s == len(R):
                    R.append(adn2)
    return len(R),R

for i in range(len(comb)):
    adn1 = comb[i]
    if nb(adn1)[0]>=96:
        print(nb(adn1)[1])
    

    
print(nb(adn1))     
        
        
        
        