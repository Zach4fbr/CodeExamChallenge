# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:12:21 2020

@author: Zacharie
"""

nmin = 5300
nmaxi = 5500
R = []


for i in range(nmin,nmaxi+1):     
    carre = str(i**2)
    cube = str(i**3)
    total = carre + cube
    if total.count("0") >= 1:
        if total.count("1") >= 1:
            if total.count("2") >= 1:
                if total.count("3") >= 1:
                    if total.count("4") >= 1:
                        if total.count("5") >= 1:
                            if total.count("6") >= 1:
                                if total.count("7") >= 1:
                                    if total.count("8") >= 1:
                                        if total.count("9") >= 1:
                                            R.append(i)
