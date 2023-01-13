# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:11:20 2022

@author: Zacharie
"""

fichier = open("C:/Users/Zacharie/Desktop/PyDéfi/Le Norn le plus adapté.txt","r")
lignes = fichier.readlines()
fichier.close()

L = []
for x in lignes:
    L.append(x)

L2=[]
for i in range(len(L)):
    L2.append(L[i].split(" -> "))

for i in range(len(L2)):
    L2[i][1] = L2[i][1].replace('\n',"")
    
def Norn(ch,L):
    r = ""
    for i in range(len(ch)-1):
        syl = ch[i]+ch[i+1]
        for x in L:
            if syl==x[0]:
                r+=ch[i]+x[1]
    r+=ch[-1]
    return r
        
ch = "GCATACGAACATT"
n = 267

for i in range(n):
    ch = Norn(ch,L2)
    if i%15==0:
        print(i)
    