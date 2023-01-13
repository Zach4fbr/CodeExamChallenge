# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:31:21 2020

@author: Zacharie
"""

#n1 = 424
#n2 = 493

L = [i for i in range(0,10)] + [1,0]
s = 0

for i in range(11,1000):
    #centaine, dizaine, unité
    c = i//100 
    d = i//10 - 10*(i//100) 
    u  = i - 10*(i//10)
    if c != 0:
        L.append(c)
    L.append(d)
    L.append(u)
    
for i in range(424,493+1):
    s += L[i]

print(L)
print(s)