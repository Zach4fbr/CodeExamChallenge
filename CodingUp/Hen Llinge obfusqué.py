# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:26:42 2022

@author: Zacharie
"""

t = "GwboOBynaABlnNecCigGdd"
txt = "MzZfiIFmMpPizwWZkbByYKfFjJkKusSbBUplLqisSlLdDIQPnrRnuUuUsgkKfFdDGSxhHmMmMXgGjaAJpzZpeEPPnNpncmMinNIwpPWfFcCCNPnqQxXNeqQhHraefFEdkKDpmMPARaqQqQikjJKmMoOIrRpPoOnNmyYMfFxXkoOsSKzZwefFEWvV yYyYjJpPEviIzeExXZxgGwWjkKJXmMxXVvVkqQoOagxXGeEAoOpPtTntTNnNKjtTxXwWgGJunjJdDoONUspPSutTtgGTUhHqlLrRQmuUjJnwfFWNxXpzZPyYlLzZMoOnweEfFWkwpPjJWnNxXKyYjJyYfFuUicbBCcCpuUoOPoeEoOsgwWsaAsSSjJGkKeEnNSpPvVsmyYMoOsSSOxXdyqQzZmMmMYnNDd"

def hen(t):
    t2 = ""
    S = []

    i = 0
    while i < len(t)-1:
        if t[i]!=t[i+1]:
            if t[i].lower() == t[i+1] or t[i].upper() == t[i+1]:
                S.append([i,i+1])
                i += 1
        i += 1
    T = []
    for i in range(len(S)):
        for j in range(len(S[i])):
            T.append(S[i][j])
    for i in range(len(t)):
        if i not in T:
            t2 += t[i]
    return t2

for i in range(5):
    t = hen(t)
    txt = hen(txt)
    print(txt)
print(txt)
print(t)


        