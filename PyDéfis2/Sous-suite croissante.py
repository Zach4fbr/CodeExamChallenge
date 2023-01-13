# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:14:18 2021

@author: Zacharie
"""

S = (-34, -16, 14, 1, -10, -29, 19, 16, -15, -19, -7, -26, -36, 14, -32, -18, -16, 18, -18, 30, 23, -12, 8, -18, -28, 18, -29, 5, 21, 28, 19, -26, -21, 37, 16, -29, 36, -10, 37, -4, -33, -18, -7, -20, -28, 35, -3, -15, -23, -40, 33, 0, 17, 39, -16, -7, 25, -32, 16, 3, -9, 33, 3, 39, -31, -29, -39, 39, 20, 33, 35, 29, -36, -29, -35, 11, 2, -40, 26, -6, -7, 20, 36, 12, 25, -24, 3, -19, 29, 20, 13, -3, 4, -36, 25, 14, -25, 1, -4, -23)

def plus_grande_sequence_position_k(E, k=None):
    if k is None:
        k = len(E)-1
    if k == 0:
        return [[0]]
    else :
        S = plus_grande_sequence_position_k(E, k-1)

        best = []
        for j,s in enumerate(S):
            if len(s) > len(best) and E[k] >= E [s[-1]]:
                best = s
        best = best + [k]
        S.append(best)
        return S

def plus_grande_sequence(E):
    if len(E) == 0:
        return E
    S = plus_grande_sequence_position_k(E)
    best = []
    for s in S:
        if len(s) > len(best):
            best = s
    return best

b = plus_grande_sequence(S)
print("E",S,"indice:",b, "valeurs:", [ S[i] for i in b ])