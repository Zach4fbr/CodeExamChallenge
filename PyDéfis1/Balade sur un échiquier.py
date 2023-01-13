# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:49:45 2021

@author: Zacharie
"""

from defisurl import DefisUrl

# Connexion au défi et récupération des entrées 
d = DefisUrl('https://pydefis.callicode.fr/defis/BaladeEchiquier/get/Zach4/f3fb2', verify=True) # Mettez votre URL personnalisée ici
lignes = d.get()

# Affichage pour contrôle :
print("\n".join(lignes))

# À vous de travailler pour calculer la réponse :
instr = lignes[0]

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

def avancer(case, rota):
    x,y = case
    if rota == 0:
        return (x,y+1)
    elif rota == 1:
        return (x+1,y)
    elif rota == 2:
        return (x,y-1)
    else:
        return (x-1,y)

def resultat(case, n):
    lettres = ['A','B','C','D','E','F','G','H']
    return str(n) + lettres[case[0]-1] + str(case[1])

rota = 0
case = (1,1) 
visitees = [case]

for c in instr:
    if c == 'A':
        case = avancer(case,rota)
        if case not in visitees:
            visitees.append(case)
    else:
        rota = pivoter(rota, c)

res = resultat(case,len(visitees))
 


# Affichage de la réponse pour contrôle et envoi :

print(res)
rep = d.post(res)
print(rep)