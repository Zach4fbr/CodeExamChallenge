# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:42:14 2021

@author: Zacharie
"""

s = 2
S = [0,s]

for i in range(1,100):
    i = str(i)
    si = 0
    for j in range(len(i)):
        si += int(i[j])
    if si % 7 == 0:
        s -= 7
    else:
        s += 2
    i = int(i)
    S.append(s)
    
print(S)
#59