# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:49:43 2021

@author: Zacharie
"""
#200 tour de boucle 10*60/3

val = 10
n = 0
e = 0
Alea = []
N = [0]
E = [0]


for i in range(0,600,3):
    val = str(val)
    if val[-1] == '0': #de 1 m vers le nord si le chiffre des unités est 0
        n += 1
        N.append(n)
        E.append(e)
    elif val[-1] == '1': #de 1 m vers l'est si le chiffre des unités est 1
        e += 1
        E.append(e)
        N.append(n)
    else: # de 1 m dans la même direction que la dernière direction prise sinon
        if N[len(N)-1] == N[len(N)-2]+1:
            n += 1
            E.append(e)
            N.append(n)
        else:
            e += 1
            E.append(e)
            N.append(n)
    val = int(val)        
    Alea.append(val)    
    val = (137 * val + 187) % 256

print((N[-1],E[-1]))