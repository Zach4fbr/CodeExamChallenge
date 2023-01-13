# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:19:45 2021

@author: Zacharie
"""

ch = 'bbbabaaaaaababaabbbababbaaaaabbabaabaabbaaababbbabababaabbbababbababaabbbaaabbabababbabbbbbaaabbbabbbabbabbbaabaabbababbabbaabbabbaaabaababbababbabbaabaaaaababaabbbabbabbaabbbbabbbabbabaaabbabbbbbabbabbaaabaaaaababbababbbabbabbbbbbbbaaabaabbabaabaaabababbababbbbbbbababbabaaabaaaaabbbabbabaaaaabbbabbaabaa'
L = []

def noeud0(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(0)
            return noeud2(i+1)
        else:
            L.append(1)
            return noeud1(i+1)
            
def noeud1(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(1)
            return noeud1(i+1)
        else:
            L.append(0)
            return noeud2(i+1)

def noeud2(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(1)
            return noeud1(i+1)
        else:
            L.append(0)
            return noeud3(i+1)

def noeud3(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(0)
            return noeud5(i+1)
        else:
            L.append(1)
            return noeud3(i+1)
        
def noeud4(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(0)
            return noeud1(i+1)
        else:
            L.append(1)
            return noeud5(i+1)
    
def noeud5(i):
    global L
    if i<len(ch):
        if ch[i] == 'a':
            L.append(1)
            return noeud4(i+1)
        else:
            L.append(0)
            return noeud4(i+1)
        
def decrypte(L):
    R = []
    for i in range(0,len(L),5):
        r = ""
        for j in range(i,i+5):
            r += str(L[j])
        R.append(r)
    return R
        
def nb(octet):
    return int(octet, 2)

def alphabet(nb):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_____"
    if nb == 0:
        return " "
    return abc[nb-1]

noeud0(0)
a = decrypte(L)

R = ""
for i in range(len(a)):
    nombre = nb(a[i])
    alpha = alphabet(nombre)
    R += alpha
    
print(R)
        