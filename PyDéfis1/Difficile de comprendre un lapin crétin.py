# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 04:42:05 2022

@author: Zacharie
"""

file = open("C:/Users/Zacharie/Desktop/PyDéfi/Difficile de comprendre un lapin crétin.txt",'r')
ch = file.read()
file.close()

ch2 = ch.split("\n")
ch = ""
for x in ch2:
    ch += x

#ch = "BWAYABWANAHBWAIAEBWAPABWAMABWAZALBWAPABWALALBWAGABWAQABWAEAOBWAEABWAYA"

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

S = []
for x in a:
    s = "BWA"+x+"A"
    S.append(s)

i=0
R = []
while i<len(ch):
    s = ""
    for j in range(i,i+5):
        s += ch[j]
    if s in S:
        i += 5
    else:
        R.append(ch[i])
        i += 1

rep = ""
for x in R:
    rep += x
print(rep)