# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:48:32 2020

@author: Zacharie
"""

F = [0,1]
s = 0
r = 0

for i in range(2,1000):
    F.append(F[i-1] + F[i-2])

for i in range(len(F)):
    F[i] = str(F[i])
    s = 0
    for x in F[i]:
        s += eval(x)
    if s == 61:
        r = i

print(r)
print(F[r])