# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:55:48 2021

@author: Zacharie
"""

x = 13

def nouv():
    global x
    lat = x%8 +2
    long = x%11 + 44
    L = (x,lat,long)
    x = (16807 * x) % 4294967295
    return L
    
L = []
n = 500

for i in range(n):
    L.append(nouv())

def affiche(lat,long):
    a = "46°34'"+str(lat)+"''"
    b = "0°22'"+str(long)+"''"
    print(a+" "+b)

N = [174, 28, 27, 479, 401, 291]
for i in range(len(N)):
    n = N[i]
    affiche(L[n][1],L[n][2])