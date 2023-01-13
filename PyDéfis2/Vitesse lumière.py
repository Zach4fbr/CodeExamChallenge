# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:59:48 2020

@author: Zacharie
"""

x,y,z = 997, 312, 663

while 10 * x > y :
    x = (y * z) % 10000
    y = (3 * z) % 10000
    z = (7 * z) % 10000 
print(x, y, z)