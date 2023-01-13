# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:31:58 2020

@author: Zacharie
"""

def Ordre66():
    L = [0,0,0,0]
    p = 0
    s = 0
    c = 0 # compteur
    c2 = 0
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    L = [i,j,k,l]
                    if L[3]>L[2]>L[1]>L[0] and L[3]%2 == L[2]%2 == L[1]%2 == L[0]%2 == 1:
                        p = L[3]*L[2]*L[1]*L[0]
                        P = [int(x) for x in str(p)]
                        for m in range(len(P)):
                            if P[m] % 2 == 1: #le nombre est impair
                                c += 1
                        if c == len(P)-1:
                            s = L[3]+L[2]+L[1]+L[0]
                            S = [int(x) for x in str(s)]
                            for m in range(len(S)):
                                if S[m] % 2 == 0: #le nombre est pair
                                    c2 += 1
                            if c2 == len(S)-1:
                                n = 1000*L[0]+100*L[1]+10*L[2]+L[3]
                                return n
                        
#réponse 1579
#on peut dénombrer les résultats
#1357
#1359
#1379
#1579
#3579

def autre():
    n1 = [1,3,5,7]
    n2 = [1,3,5,9]
    n3 = [1,3,7,9]
    n4 = [1,5,7,9]
    n5 = [3,5,7,9]
    p1 = 1*3*5*7
    p2 = 1*3*5*9
    p3 = 1*3*7*9
    p4 = 1*5*7*9
    p5 = 3*5*7*9
    s1 = 1+3+5+7
    s2 = 1+3+5+9
    s3 = 1+3+7+9
    s4 = 1+5+7+9
    s5 = 3+5+7+9 
    return 1579
        
            
print(autre())