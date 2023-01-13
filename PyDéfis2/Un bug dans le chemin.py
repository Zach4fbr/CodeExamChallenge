# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:54:37 2021

@author: Zacharie
"""

import numpy as np

instr = "GAADAGDAAGDAAGDGGADGAAGAAAGGDAADAGDGDGADDAGDDAADGAGAGDDAGDGDAAGDDAAGAAGDDDDGADGAAAGAGGDGDGDGDAGAAGGGADAADGADGDGAGAGGAGGGAGDADAADGGGAGADDGDDAAAGGAGADAAAADGAGGGDAAGADADAADAGAAAGADDDDADDDDDAGGAGAAGDGDAGAADDGADGDDAGDDGDDGDGAGDGGDAGAGDGGDGGGDADAGDADGGGADDDGGGAAAGGDDAAGAAGAADGGDAGDGDAGDDGDDADDGGGAGDDAGDGDAGGAAGADADADGDDDDADDAGDGGDADAAADGGGGAGGGGDDGAAAAGDDDGDAGDAAADGAAGGGDGDDDGAAGDGGAGGDDDADGADAGGAAAAGAADGGAAAGGGGDDDDGAAGDDADDAGDADDDAADGDGAGGGGGDGDGAGDAGADDAGGAGDAGAGDAAAGDADGGAAGDGDDDGADGAAAGDGDDADGGGA"

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

def distance(case):
    return np.sqrt(case[0]**2+case[1]**2)
    
R = []

for i in range(len(instr)):
    ch = instr
    if ch[i] == "A":
        ch = instr[:i] + "G" + instr[i+1:]
        R.append(ch)
        ch = instr[:i] + "D" + instr[i+1:]
        R.append(ch)
    if ch[i] == "D":
        ch = instr[:i] + "A" + instr[i+1:]
        R.append(ch)
        ch = instr[:i] + "G" + instr[i+1:]
        R.append(ch)
    if ch[i] == "G":
        ch = instr[:i] + "A" + instr[i+1:]
        R.append(ch)
        ch = instr[:i] + "D" + instr[i+1:]
        R.append(ch)
    
    
def caseETdist(instr):
    rota = 0
    case = (0,0) 
    
    for c in instr:
        if c == 'A':
            case = avancer(case,rota)
        else:
            rota = pivoter(rota, c)
    return case,distance(case)*100    

R2 = []
for x in R:
    a = caseETdist(x)
    R2.append(a)

M = 0    
for i in range(len(R2)):
    if R2[i][1]>M:
        M = R2[i][1]
print("nb de chemin :",len(list(set(R2))),"Maxi :",M)

