# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:30:28 2021

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

def hashe(l):
    a=sorted(set(l), key=l.index)
    return a

def power(n,l):
    a=l.count(n)
    return a

def final(n):
    p=prime_factors(n)
    a=hashe(p)
    x=""
    for i in range(len(a)):
        if power(a[i],p) != 1:
            x=x+(str(a[i])+'^'+'{'+str(power(a[i],p)))+'}'
        else:
            x=x+(str(a[i]))
        if i !=len(a)-1:
            x=x+'x'
    return x

def frugal(n):
    p = final(n)
    n = str(n)
    m = len(n)
    s = 0
    for i in range(len(p)):
        for j in range(100):
            if p[i] == str(j):
                s+=1
    if s >= m:
        return False
    else:
        return True
            
    
N = []
for i in range(123456,165432+1):
    if i%100 == 0:
        print(i)
    if frugal(i)==True:
        N.append(i)