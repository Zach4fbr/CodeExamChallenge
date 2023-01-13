# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:33:58 2020

@author: Zacharie
"""

n = 39

M=[[17, 3, 4, 14, 5, 17], [8, 16, 3, 17, 14, 12], [13, 5, 15, 4, 16, 3], [14, 7, 3, 16, 3, 2], [6, 1, 16, 10, 5, 13], [11, 1, 9, 11, 18, 8]]

s = 0

for k in range(n):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = (9*M[i][j]+3)%19
            
for i in range(len(M)):
    for j in range(len(M[i])):
        s += M[i][j]
    
print(s)