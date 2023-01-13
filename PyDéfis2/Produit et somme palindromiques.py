# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:57:31 2021

@author: Zacharie
"""

def palindrome(n):
    n = str(n)
    if n[::-1] == n:
        return True
    return False
        

mini = 12
maxi = 82

i=0

for a in range(mini,maxi+1):
    s = 0
    p = 0
    for b in range(mini,maxi+1):
        for c in range(mini,maxi+1):
            for d in range(mini,maxi+1):
                if a<=b and b<=c and c<=d:
                    s = a+b+c+d
                    p = a*b*c*d
                    if palindrome(s)==True and palindrome(p)==True:
                        i+=1

print(i)
