# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:41:07 2021

@author: Zacharie
"""

def gibi(nb):
    if nb == 0:
        return 'KWA'
    if nb == 1:
        return 'BY'
    if nb == 2:
        return 'TU'
    if nb == 3:
        return 'NEU'

def num(n):
    if n == 0:
        return ""
    else:
        r = n%4
        return num(n//4)+gibi(r)

L = [207, 333, 204, 351, 112, 241, 236, 111, 312, 191]
R = []
for i in range(len(L)):
    R.append(num(L[i]))
    