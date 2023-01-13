# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:49:13 2021

@author: Zacharie
"""

S = []

for n in range(1,201):
    
    def vif_or(x,y,z):
        return (y,z,(x+y+z)%n)
    
    L = [(0,0,1)]
    for i in range(1,100000):
        x,y,z = L[i-1][0],L[i-1][1],L[i-1][2]
        a = vif_or(x,y,z)
        L.append(a)
        i += 1
    
    s = 0
    
    for i in range(1,len(L)):
        if L[i]==L[0]:
            s = i
            break
    S.append([s,n])

S = sorted(S)
p = len(S)
print(S[p-10:])

#142,183,161,138,178,179,191,165,177,195