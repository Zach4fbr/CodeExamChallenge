# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:55:40 2021

@author: Zacharie
"""

n = 131*4
a = 20 #7,11,13kg
N=[]
for i in range(a+1):
    for j in range(a+1):
        for k in range(a+1):
            if i*7+j*11+k*13 == n:
                N.append([i,j,k])
                
S = []

for i in range(len(N)):
    s = 0
    for j in range(len(N[i])):
        s+=N[i][j]
    S.append(s)
    
            