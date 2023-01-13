# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:03:04 2020

@author: Zacharie
"""

O = []
#somme de nb = 11
R = []
#résultat

for i in range(0,1000):
    if i//100 + (i//10 - 10*(i//100)) + (i - 10*(i//10 - 10*(i//100)) - 100*(i//100)) == 11:
        O.append(i)
        if i % 7 == 0:
            R.append(i)
print(R)