# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:20:10 2020

@author: Zacharie
"""

T = []
t = 8188



for i in range(1000):
    t = t//2
    if t % 2 == 1: #le nombre de tête est impair
        t = 3*t+1
    if t == 2:
        T.append(2)
        t = 1
    T.append(t)