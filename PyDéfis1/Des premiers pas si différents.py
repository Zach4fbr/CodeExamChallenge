# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:21:24 2021

@author: Zacharie
"""

import math as np

def premiers(n):
  prem=list(range(2,n+1))
  k=2
  nRacine=np.sqrt(n)
  while k<nRacine:
    prem=[p for p in prem if p<=k or p%k!=0]
    k=prem[prem.index(k)+1]  # nouveau nombre premier
  return prem

P = premiers(10000000)
n = 90

R = []
for i in range(len(P)-1):
    if P[i+1]-P[i]==n:
        R.append(P[i+1])


