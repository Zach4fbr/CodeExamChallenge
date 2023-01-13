# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:22:48 2020

@author: Zacharie
"""

u = '2963'
n = 105
r = 0
N = [int(u)]

for i in range(n-1):
    if len(u)==4:
        n2 = int(u[0:2]) + int(u[2:4])
        n2 = 188*n2 + 188
        r = n2 % 9973
        N.append(r)
        u = str(r)
    if len(u)==3:
        n2 = int(u[0]) + int(u[1:3])
        n2 = 188*n2 + 188
        r = n2 % 9973
        N.append(r)
        u = str(r)
    if len(u)==2:
        n2 = int(u[0]) + int(u[1])
        n2 = 188*n2 + 188
        r = n2 % 9973
        N.append(r)
        u = str(r)
    if len(u)==1:
        n2 = int(u[0])
        n2 = 188*n2 + 188
        r = n2 % 9973
        N.append(r)
        u = str(r)
        
#réponse 358