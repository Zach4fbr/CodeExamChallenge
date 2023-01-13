# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:26:43 2020

@author: Zacharie
"""

#n = 13*a + 7*b

n = 3188
S = []

for a in range(n):
    for b in range(n):
        if 13*a + 7*b == n:
            print(abs(b-a))
            S.append([a,b])