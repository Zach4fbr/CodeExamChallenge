# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:59:32 2021

@author: Zacharie
"""

def pièces(n):
    L = [50,20,10,5,2,1]
    S = []
    for i in range(len(L)):
        if n//L[i] == 0:
            S.append(n//L[i])
        else:
            S.append(n//L[i])
            n -= n//L[i]*L[i]
    return S

N = [47, 13, 19, 62, 84, 32, 50, 42, 91, 93, 34, 19, 92, 35, 19, 4, 17]
S = [0,0,0,0,0,0]
for i in range(len(N)):
    L = pièces(N[i])
    for j in range(len(L)):
        S[j] += L[j]
print(S)