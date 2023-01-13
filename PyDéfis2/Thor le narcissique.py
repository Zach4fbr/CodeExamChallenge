# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:10:46 2021

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/TD Info PT/Entrainement/PyDéfi/Thor le narcissique.txt","r")
lignes = fichier.readlines()
fichier.close()

n = len(lignes)
R = []

from collections import Counter
#my_str = "Mary had a little lamb"
#counter = Counter(my_str)
#print(counter['a'])

for i in range(n):
    counter = Counter(lignes[i])
    if counter['t'] == 1 and counter['h'] == 1 and counter['o'] ==1 and counter['r'] == 1:
        R.append(lignes[i])
    
print(len(R))
