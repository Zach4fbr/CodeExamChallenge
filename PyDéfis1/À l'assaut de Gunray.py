# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:29:19 2020

@author: Zacharie
"""

t = 0
V = 0
s = 0

while s <= 35:
    E = 3-0.005*V
    V += E*8
    s += E
    t += 1

#t = 16
#t = 67