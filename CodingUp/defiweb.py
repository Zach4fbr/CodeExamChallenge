# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 09:36:58 2022

@author: Zacharie
"""

from defisurl import DefisUrl
# Connexion au défi et récupération des entrées 
d = DefisUrl('https://codingup.univ-poitiers.fr/herewego/defis/ExempleURL/get/Zach4/c9d27', verify=True) # Mettez votre URL personnalisée ici
lignes = d.get()

# Affichage pour contrôle :
print("\n".join(lignes))

# À vous de travailler pour calculer la réponse :
res = int(lignes[1]) + int(lignes[0]) # On met ici 0, ce qui n'est probablement pas la bonne réponse...

# Affichage de la réponse pour contrôle et envoi :
print(res)
rep = d.post(res)
print(rep)