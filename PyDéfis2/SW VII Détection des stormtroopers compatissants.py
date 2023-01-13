# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:16:03 2021

@author: Zacharie
"""

from collections import Counter

def chiffre(n):
    m = str(n)
    for i in range(1,n):
        for j in range(i,n):
            if i*j <= 10000 and i*j >= 1000:
                p = str(i)+str(j)
                if i*j == n and Counter(m) == Counter(p):
                    return n
    return None


N = []
for i in range(1,10000):
    if chiffre(i) != None:
        N.append(i)
    print(i)
        
#1206, 1255, 1260, 1395, 1435, 1503, 1530, 1827, 2187, 3159, 3784 de 1 à 5000

#6880 de 5000 à 10000
    
    

    
            