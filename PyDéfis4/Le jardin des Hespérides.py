# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:31:50 2021

@author: Zacharie
"""

import numpy as np

n = 142

def est_pair(n):
    if n%2 == 0:
        return True
    else:
        return False

def divisible_3(n):
    if n%3 == 0:
        return True
        
S = [n]    

while n != 1:
    if est_pair(n)==True:
        n = n//2
        S.append(n)
    else:
        n = 3*n+1
        S.append(n)

s = 0
#np.sqrt(2**2+19**2) OUT 19.1049731745428


H = [0,0]   #Hercule
Orientation = ['N','E','S','O']*10
M = []
j = 0
for i in range(len(S)-1):
    if est_pair(S[i]) == False:
        if divisible_3(S[i]) == True:
            j = j+1
        else:
            j = j-1
    else:
        M.append(Orientation[j])

print(M)

for i in range(len(M)):
    if M[i]=='N':
        H[1] += i+1
    if M[i]=='E':
        H[0] += i+1
    if M[i]=='S':
        H[1] -= i+1
    if M[i]=='O':
        H[0] -= i+1
    
print(H)
print(np.sqrt(H[0]**2+H[1]**2)*1000) #réponse en m

    
    
    