# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:54:27 2021

@author: Zacharie
"""

u = 53
n = 21


for i in range(n):
    t = 0
    u = bin(u)[2:]
    s = 0
    for x in u:
        if x == '1':
            s += 1
    s = bin(s)[2:]
    t = '0b'+ u + s
    u = int(t,2)
