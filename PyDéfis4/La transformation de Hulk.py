# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:26:06 2021

@author: Zacharie
"""

#le brutforce ne marche pas ici

A = [1,0,0,0,0,0,0]

def hulk(L):
    
    if L[0]!=0:
        L[0]-=1
        L[1]+=1
    if L[1]!=0:
        L[1]-=1
        L[0]+=1
    if L[2]!=0:
        L[2]-=1
        L[0]+=1
    return L


s = 0
for i in range(31,24,-1):
    s+=2**i
print(s)