# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:45:14 2021

@author: Zacharie
"""

n = 3000
T = ""
n1 = 2065
n2 = 2091
#début 0110100110010110
    
O = [0]*n

for i in range(n//2):
    O[2*i] = O[i]
    O[2*i+1] = 1-O[i]

for i in range(len(O)):
    T += str(O[i])
    
S = ""
for i in range(n1,n2+1):
    S += T[i]


