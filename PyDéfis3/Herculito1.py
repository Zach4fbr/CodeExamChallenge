# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:17:53 2021

@author: Zacharie
"""

L = ("ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE SELENE THEMIS THETIS TRITON ZEUS").split()

def nombre(a):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(abc)):
        if abc[i] == a:
            return 1+i

def valeur(mot):
    s = 0
    for x in mot:
        s += nombre(x)
    return s

N = []
for i in range(len(L)):
    N.append(valeur(L[i]))
    
T = []
for i in range(len(N)):
    T.append([L[i],N[i]])
    
def f1(elem):
    return elem[1]

T.sort(key=f1)

for i in range(len(T)):
    print(T[i][0], end = " ")
    