# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:36:29 2021

@author: Zacharie
"""

L = [20,20,20,0]

def vidange(L,n):
    a = float(format(L[n]/3,".2f"))
    if L[(n+1)%4]+a > 25:
        L[n%4] = L[n%4]-(25-L[(n+1)%4])
        L[(n+1)%4] = 25
    else:
        L[n%4]-=a
        L[(n+1)%4]+=a 
    a = float(format(L[n]/3,".2f"))
    if L[(n+2)%4]+a > 25:
        L[n%4] = L[n%4]-(25-L[(n+2)%4])
        L[(n+2)%4] = 25
    else:
        L[n%4]-=a
        L[(n+2)%4]+=a
    a = float(format(L[n]/3,".2f"))
    if L[(n+3)%4]+a > 25:
        L[n%4] = L[n%4]-(25-L[(n+3)%4])
        L[(n+3)%4] = 25
    else:
        L[n%4]-=a
        L[(n+3)%4]+=a
    return L
    
    
        
        
for i in range(12):
    n = i%4
    L = vidange(L,n)
print(L)