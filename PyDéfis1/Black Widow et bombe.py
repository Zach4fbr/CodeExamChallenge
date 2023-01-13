# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:04:39 2020

@author: Zacharie
"""

#n = 797114
U = 797
N = 114
u = 0

for i in range(N):
    U = 13*U 
    u = U - 1000*(U//1000)
    U = u
    