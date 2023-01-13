# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:47:42 2020

@author: Zacharie
"""

"""Q(1)=1
Q(2)=1
Pour n>2, Q(n)=Q(n-Q(n-1))+Q(n-Q(n-2))"""

nmin = 1583
nmax = 1697

Q = [1,1]


for n in range(2,2000):
    Q.append(Q[n-Q[n-1]]+Q[n-Q[n-2]])

s = 0

for i in range(nmin-1,nmax):
    s += Q[i]
    
print(s)