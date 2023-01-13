# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:12:19 2021

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/La chambre des pairs.txt")
ligne = fichier.read()
fichier.close()

ABC = ["A","B","M","D","E","F","L","H","I","J","R","G","N","C","O","Q","P","K","S","Y","U","V","W","X","T","Z"]
N = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def est_paire(car):
    if car == "/":
        return True
    for i in range(len(ABC)):
        if car==ABC[i]:
            if N[i]%2==0:
                return True
            else:
                return False
    n = int(car)
    if n%2 == 0:
        return True
    else:
        return False

S = ""
for i in range(len(ligne)):
    p = est_paire(ligne[i])
    if p == True:
        S += ligne[i]
    else:
        S += ","
        
N = S.split(',')
m = 0 
j = 0
for i in range(len(N)):
    if len(N[i])>m:
        m = len(N[i])
        j = i

print(N[j])
    

