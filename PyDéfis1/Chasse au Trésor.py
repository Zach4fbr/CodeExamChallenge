# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:32:52 2021

@author: Zacharie
"""

fichier = open("C:\\Users\\Zacharie\\Desktop\\PyDéfi\\Chasse au Trésor.txt",'r')
ligne = fichier.read()
fichier.close()

L = ligne.split(',')
R = []

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
    
#for c in L:
#    if c[0] == 'A':
#        case = avancer(case,rota,int(c[2:]))
#    else:
#        rota = pivoter(rota, c)

for c in L:
    if c[0] == 'A':
        case = avancer(case,rota,int(c[2:]))
    else:
        rota = pivoter(rota, c)

print(case)
