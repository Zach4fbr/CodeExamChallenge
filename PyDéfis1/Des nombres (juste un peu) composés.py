# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:34:24 2021

@author: Zacharie
"""

import numpy as np

#def decomposition(n):
#    "donne la décomposition en facteurs premiers de n"
#    diviseur,i={},2
#    while n!=1:
#        if n%i==0:
#            if i in diviseur:
#                diviseur[i]+=1
#            else:
#                diviseur[i]=1
#            n/=i
#            i=2
#        else:
#            i+=1
#    return diviseur

def primalite(a):
    "renvoie si un nombre est premier"
    for i in range(2,int(np.sqrt(a)+1)):
        if a%i==0:
            return False
    return True


def rechercheP(n):
    premiers = []
    for i in range(2,n+1):
        if primalite(i):
            premiers.append(i)
    return premiers

n = 8000

P = rechercheP(n)
P2 = []
for i in range(len(P)):
    for j in range(i+1,len(P)):
        P2.append(P[i]*P[j])
            
P2 = sorted(P2)

P3 = []
for i in range(200):
    for j in range(i+1,200):
        for k in range(j+1,200):
            P3.append(P[i]*P[j]*P[k])
P3 = sorted(P3)

R = P2+P3
R = sorted(R)





