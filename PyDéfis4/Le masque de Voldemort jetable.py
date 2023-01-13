# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:47:29 2021

@author: Zacharie
"""

import base64

texte = "TUSAISQUI"
message = []
for i in range(len(texte)):
    message.append(ord(texte[i]))
    
def v(a,b,x):
     return (a*x+b)%256

a = 17
b = 37
x = 73

def N(a,b,x):
    N = [x]
    for i in range(len(message)+10):
        x = N[i]
        N.append(v(a,b,x))
    return N

def binaire(N):
    B = []
    for i in range(len(N)):
        a = bin(N[i])[2:]
        n = len(a)
        a = (8-n)*"0"+a
        B.append(a[:5])
    return B
    
def bitstring(B):
    b = ""
    for i in range(len(B)):
        b += B[i]
    return b

def key(b):
    clé = []
    for i in range(0,len(b),8):
        a = int(b[i:i+8],2)
        clé.append(a)
    return clé

def chiffre(clé):
    chiffré = []
    for i in range(len(clé)):
        chiffré.append(message[i]^clé[i])
    return chiffré
 
def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
