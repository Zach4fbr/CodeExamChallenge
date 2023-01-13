# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:55:09 2020

@author: Zacharie
"""

b = 0
r = 0
n = 0
T = []

ntot = 0

for i in range(1000):
    b = i
    print(i)
    for j in range(1000):
        r = j
        for k in range(1000):
            n = k
            ntot = b+r+n
            if b <= r <= n and b*r*n == 777*ntot and n <= 2*b:
                T.append(b)
                T.append(r)
                T.append(n)
                
ntot = 37+50+63