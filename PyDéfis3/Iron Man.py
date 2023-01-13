# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:32:27 2020

@author: Zacharie
"""

n = 1435
s = 0

for i in range(0,n):
    if i % 3 == 0:
        s += i
    if i % 5 == 0:
        if i % 3 != 0:
            s += i
print(s)