# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:37:47 2021

@author: Zacharie
"""

fichier=open("C:/Users/Zacharie/Desktop/PyDéfi/Séquence Chiffrée.txt","r")
lignes = fichier.readlines()
fichier.close()

n = len(lignes)

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chc = "MDLPHELHQUHOHYHUGHVGHILVDYHFSBWKRQ"
chc2 = ""
d = -3 #décalage

def position(x):
    for i in range(len(ABC)):
        if x == ABC[i]:
            return i
        
def lettre(n):
    return ABC[n]

#SECRET et TROUVER
"""for i in range(len(chc)):
    p = position(chc[i])
    if p + d >= 26:
        a = p-d
    else:
        a = p+d
    z = lettre(a)
    chc2 = chc2 + str(z)    
print(chc2)"""

for k in range(1,len(lignes)//2):
    chc = lignes[k][:50]
    for d in range(-25,25):
        for i in range(len(chc)):
            p = position(chc[i])
            if p + d >= 26:
                a = p-d
            else:
                a = p+d
            z = lettre(a)
            chc2 = chc2 + str(z) 
        chc2 += " "
    #print(chc2)
    x = chc2.find('SECRET')
    y = chc2.find('TROUVER')
    if x != -1 and y != -1:
        rep = chc2
        #print(k)
    else:
        chc2 = ""
print(x)
print(y)
#print(rep)
print(chc2[y-30:x+20])
