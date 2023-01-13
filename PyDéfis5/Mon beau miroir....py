# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:45:47 2020

@author: Zacharie
"""

"""Vous avez l'assurance que pour tout nombre de départ proposé, 
vous atteindrez forcément un palindrôme en au plus 100 additions.""" #Oups


def Miroir(n,i):
    a = str(n)
    b = a[::-1]
    s = int(a)+int(b)
    if Palindrome(s)==True:
        return [s,i+1]
    else:
        i += 1
        a = str(s)
        b = a[::-1]
        return Miroir(s,i)


def Palindrome(n):
    n = str(n)
    for i in range(len(n)):
        if n[::] == n[::-1]:
            return True
        else: 
            return False

R = []

L = [396, 294, 290, 861, 481, 194, 570, 463, 265, 935]
for i in range(len(L)):
    m = Miroir(L[i],0)
    R.append(m)

print(R)