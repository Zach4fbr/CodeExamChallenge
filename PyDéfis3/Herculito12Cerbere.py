# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:19:01 2021

@author: Zacharie
"""

n = 13979

N=[]

for i in range(n):
    print(i)
    for j in range(n):
        if i**2+j**2==n**2:
            N.append([i,j])

M = 0
for i in range(len(N)):
    if N[i][1] > M:
        M = N[i]
print(M)