# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:03:10 2021

@author: Zacharie
"""

def Ministere(ch):
    a,b,c,d,e,s = 0,0,0,0,0,0
    for x in ch:
        if x=='1':
            a += 1
        elif x=='2':
            b += 1
        elif x=='4':
            c += 1
        elif x=='6':
            d += 1
        elif x=='7':
            e += 1
        else:
            s += 1
    if s != 0:
        return False
    if a==0 or b==0 or c==0 or d==0 or e==0:
        return False
    return True

n = 64224
R = []

for i in range(n,2*n):
    if Ministere(str(i**2))==True:
        R.append(i)