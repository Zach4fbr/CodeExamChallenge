# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:10:52 2020

@author: Zacharie
"""

#tour 324 mètres soit 32400 cm

x = 1170 #cm
y = 290 #cm



D = [x]
S = []
s = 0

for i in range(1,1000):
    if i % 5 == 0:
        D.append(D[i-2]-4)
    else:
        D.append(D[i-1] + x-2*i - y)
    for j in range(len(D)):
        s += D[j]
    S.append(s)
    
    
print(D)