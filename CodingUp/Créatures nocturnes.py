# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:04:26 2022

@author: Zacharie
"""

L = [0,0,0,0] #c,s,z,f
H = [2,1,1,1]

for i in range(1,3001): #n-1 secondes
    if i%2 == 0:
        L[0] += 10
    if i%5 == 0:
        L[1] += 5
    if i%6 == 0:
        L[2] += 4
    if i%10 == 0:
        L[3] += 3
    if i%6 == 0:
        L[0] -= H[0]
    if i%20 == 0:
        L[1] -= H[1]
    if i%30 == 0:
        L[2] -= H[2]
    if i%40 == 0:
        L[3] -= H[3]
    if i%240 == 0:
        H[0] += 2
        H[1] += 1
        H[2] += 1
        H[3] += 1
        
        
print(L)