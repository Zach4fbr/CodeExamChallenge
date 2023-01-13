# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:06:53 2020

@author: Zacharie
"""

"""initialiser a, b, c, k et n respectivement à 1, 4, 3, 1 et 0
répéter tant que k est strictement inférieur à 1000-n
    a ← b
    b ← c + a
    c ← -4*c - 3*a - b
    n ← a + b
    augmenter k de 1
fin répéter"""

a,b,c,k,n = 1,4,3,1,0

while k < 1000-n:
    a = b
    b = c + a
    c = -4*c - 3*a - b
    n = a + b
    k += 1
print(a,b,c)