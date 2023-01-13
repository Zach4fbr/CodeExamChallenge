# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:49:48 2020

@author: Zacharie
"""

def prime_factors(n):
    prime = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prime.append(d)
            n //= d
        d += 1
    if n > 1:
       prime.append(n)
    return prime

def impair(n):
    if n % 2 == 1:
        return True

E = []
A = []
R = []

for i in range(10000):
    if len(prime_factors(i)) == 3:
        if prime_factors(i)[0]==prime_factors(i)[1] or prime_factors(i)[1]==prime_factors(i)[2] or prime_factors(i)[0]==prime_factors(i)[2]:
            E.append(i)
            
for i in range(len(E)):
    if impair(E[i]) == True:
        A.append(E[i])

for i in range(len(A)-3):
    if A[i+3] == A[i] + 6:
        R.append(i)
    