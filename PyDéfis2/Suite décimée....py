# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:07:55 2021

@author: Zacharie
"""

n = 395

s = 0
T = []

def nombre_4(i):
    i = str(i)
    for j in range(len(i)):
        if i[j] == '4':
            return True
    return False

for i in range(1,n+1):
    if nombre_4(i)==False:
        s += 1/i
        T.append(s)

print(T[-1])