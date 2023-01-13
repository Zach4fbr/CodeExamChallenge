# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:16:59 2022

@author: Zacharie
"""

def Hercule(chaine):
    rep = ""
    for x in chaine:
        if x == "D":
            rep += "DAGAGA"
        if x == "G":
            rep += "GADADA"
        if x == "A":
            rep += "AA"
    return rep

a = "DG"
for i in range(2):
    chaine = Hercule(a)
    a = chaine

rota = 0
case = (0,0) 

# 0 HAUT
# 1 DROITE
# 2 BAS
# 3 GAUCHE

def pivoter(rota, c):
    if c == "D":
        rota = (rota+1)%4 
    if c == "G":
        rota =(rota-1)%4
    return rota

def avancer(case, rota, nb):
    x,y = case
    if rota == 0:
        return (x,y+nb)
    elif rota == 1:
        return (x+nb,y)
    elif rota == 2:
        return (x,y-nb)
    else:
        return (x-nb,y)
    

for c in chaine:
    if c == 'A':
        case = avancer(case,rota,10)
    else:
        rota = pivoter(rota, c)

print(case)