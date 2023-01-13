# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:34:27 2021

@author: Zacharie
"""

B = [2]
R = []
V = []

n = 103
for i in range(n//3):
    r = 7*B[i]
    v = 5*B[i]
    R.append(r)
    V.append(v)
    p = r+v
    t = str(p)[-2] + str(p)[-1]
    t = int(t)
    B.append(t)
    
B.pop(0)
s = 2
for i in range(len(R)):
    s = s + R[i] + B[i] + V[i]

print(s)