# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:16:25 2020

@author: Zacharie
"""

L = [4878, 8704, 7320, 7618, 7964, 5356, 1152, 8566, 5396, 7678, 2818, 1060, 9306, 1362, 7912, 5948, 7974, 3122, 3362, 3620, 3260, 4058, 4710, 7210, 304, 6774, 738, 7644, 928, 2636, 4752, 8564, 2772, 5792, 5120, 2266, 6002, 9020, 8006, 8284, 5730, 5416, 2662, 728, 7050, 8098, 9018, 5806, 5618, 9866]

P = []
R = []
F = [[7, 4871]]

def estPremier(n) :
    if n <= 1 :
            return False
    for i in range(2, n) :
            if (n % i == 0) :
                return False
    return True

def N_Position(n,L):
    s = 0
    for i in range(len(L)):
        if L[i][0]+L[i][1]==n:
            s += 1
    return s
   

for i in range(10000):
    if estPremier(i) == True:
        P.append(i)

for i in range(len(L)):
    for x in P:
        for y in P:
            if L[i] == x + y:
                R.append([x,y])

s = 0

for i in range(len(L)-1):
    s += N_Position(L[i],R)
    F.append(R[s])
print(F)