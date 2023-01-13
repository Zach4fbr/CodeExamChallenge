# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:42:45 2020

@author: Zacharie
"""

n1 = 1245
n2 = 4198

def persistance(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        L = []
        p = 1
        for x in n:
            L.append(x)
        for i in range(len(L)):
            p *= int(L[i])   # p = p*L[i]
        return persistance(p)

P = [0,0,0,0,0,0,0,0,0,0]

for i in range(n1,n2+1):
    p = persistance(i)
    for j in range(1,len(P)):
        if p == j:
            P[j] += 1

P.pop(P[0])
print(P)

