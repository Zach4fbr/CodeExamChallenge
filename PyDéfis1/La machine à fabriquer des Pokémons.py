# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:14:15 2021

@author: Zacharie
"""

b1,b2,b3,b4,b5,b6 = 1,1,1,1,1,1


def B1():
    global b1
    if b1 == 1:
        b1 = 1+b1%3
        return B2()
    if b1 == 2:
        b1 = 1+b1%3
        return B3()
    if b1 == 3:
        b1 = 1+b1%3
        return B4()
    
def B2():
    global b2
    if b2 == 1:
        b2 = 1+b2%2
        return B5()
    if b2 == 2:
        b2 = 1+b2%2
        return B6()
    
def B3():
    global b3
    if b3 == 1:
        b3 = 1+b3%3
        return B2()
    if b3 == 2:
        b3 = 1+b3%3
        return B5()
    if b3 == 3:
        b3 = 1+b3%3
        return B6()

def B4():
    global b4
    if b4 == 1:
        b4 = 1+b4%2
        return B3()
    if b4 == 2:
        b4 = 1+b4%2
        return B6()

def B5():
    global b5
    if b5 == 1:
        b5 = 1+b5%2
        return 'R'
    if b5 == 2:
        b5 = 1+b5%2
        return 'E'
    
def B6():
    global b6
    if b6 == 1:
        b6 = 1+b6%3
        return B5()
    if b6 == 2:
        b6 = 1+b6%3
        return 'G'
    if b6 == 3:
        b6 = 1+b6%3
        return B4()

rep = ""
n = 100
for i in range(n):
    rep += B1()
print(rep)