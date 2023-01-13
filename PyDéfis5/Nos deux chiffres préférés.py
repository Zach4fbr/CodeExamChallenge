# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:55:09 2020

@author: Zacharie
"""

mini = 143
maxi = 941

N = []

for i in range(mini,maxi+1):
    i = str(i)
    for j in i:
        if j == '1' or j == '6':
            N.append(int(i))
            
N = list(set(N))

s = 0
for i in range(len(N)):
    s += N[i]

print(s)