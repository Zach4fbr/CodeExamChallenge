# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:51:26 2021

@author: Zacharie
"""

def bin2dec(ch):
    s = 0
    n = len(ch)
    for i in range(n):
        s += int(ch[i])*2**(n-i-1)
    return s

def impulsion_suivante(n):
    n = bin(n)[2:]
    n = n[::-1]
    n = bin2dec(n)+2
    return n


def période(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]==L[j]:
                return j-i
    return -1


P = []

for n in range(1,500):
    N = []
    for i in range(1024):
        N.append(impulsion_suivante(n))
        n = impulsion_suivante(n)
    p = période(N)
    P.append(p)
    
    
R = []
for i in range(len(P)):
    if P[i]!=-1:
        R.append(i+1)
        
print(R)