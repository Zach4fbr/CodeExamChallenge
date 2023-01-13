# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:57:08 2021

@author: Zacharie
"""

L = [12, 24, 31, 77, 87, 103, 112, 145, 181, 197, 205, 217, 224, 225, 228, 255, 263, 278, 289, 297]

k = 1881
s = 0
import itertools


R = []
for i in range(0,len(L)+1):
   R.append(list(itertools.combinations(L,i)))

R2 = []
for i in range(len(R)):
    for x in R[i]:
        R2.append(x)
        
s = 0
Y = []
for i in range(len(R2)):
    for j in R2[i]:
        s += j
        if s == k:
            Y.append(R2[i])
    s = 0

print(Y[100])
#print(Y[101])