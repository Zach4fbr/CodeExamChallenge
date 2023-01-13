# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:58:44 2020

@author: Zacharie
"""

x1 = 1694
y1 = 1546
n = 50

X = [x1]
Y = [y1]

for i in range(0,n):
    X.append((X[i] + 2*Y[i])%2018)
    Y.append((-3*X[i] + Y[i])%2018)

déclinaison = (X[n]-900)/10
ascension_droite = (Y[n]/150)*2

print("d =",déclinaison, "a =",ascension_droite)