# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:12:51 2020

@author: Zacharie
"""

P = []
n = 53
# p= 34k+35 (avec k supérieur ou égal à 0)
N = []
    

def estPremier(n) :
    if n <= 1 :
            return False
    for i in range(2, n) :
            if (n % i == 0) :
                return False
    return True
   
for i in range(10000):
    if estPremier(i) == True:
        P.append(i)

for i in range(len(P)):
    for k in range(1000):
        if P[i] == 34*k+35:
            N.append([P[i],k])
print(N[n-1])