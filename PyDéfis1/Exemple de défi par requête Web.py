# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:41:49 2021

@author: Zacharie
"""

from defisurl import DefisUrl

# Connexion au défi et récupération des entrées 
d = DefisUrl('https://pydefis.callicode.fr/defis/ExempleURL/get/Zach4/a6792', verify=True) # Mettez votre URL personnalisée ici
lignes = d.get()

# Affichage pour contrôle :
print("\n".join(lignes))

# À vous de travailler pour calculer la réponse :
res = int(lignes[0])+int(lignes[1]) # On met ici 0, ce qui n'est probablement pas la bonne réponse...

# Affichage de la réponse pour contrôle et envoi :

print(res)
rep = d.post(res)
print(rep)