# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:38:45 2020

@author: Zacharie
"""

L = []
mini = 8962
maxi = 9189

H = []

def heureux(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])**2
    for i in range(len(L)):
        if L[i] == s:
            return False
    if s == 1:
        return True
    else:
        print(s)
        L.append(s)
        for i in range(len(L)):
            if int(s) == L[i]:
                return heureux(s)

for k in range(mini,maxi+1):
    if heureux(k) == True:
        L = []
        H.append(k)
        
print(H)