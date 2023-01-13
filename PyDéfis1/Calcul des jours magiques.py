# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:41:20 2021

@author: Zacharie
"""

import datetime

today = datetime.date(2020, 3, 22).weekday() #date correspondant au 22 mars 2020

def int2day(n):
    D = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
    return D[n]

def magique(jour,nombre):
    n = len(jour)
    if (n+nombre)%10 == 0:
        return True
    return False

def bissextile(annee):
    if(annee%4==0 and annee%100!=0 or annee%400==0):
        return True
    else:
        return False
    
#year = 2020
#month = 3
#s = 0
def nb_magique():
    s = 0
    for year in range(2000,2025):
        for month in range(1,12+1):
            if month != 2:
                for day in range(1,30+1):
                    today = datetime.date(year, month, day).weekday()
                    jour = int2day(today)
                    if magique(jour,day) == True:
                        s += 1
                    if year == 2021 and month == 10 and day == 15:
                        return s
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    day = 31
                    today = datetime.date(year, month, day).weekday()
                    jour = int2day(today)
                    if magique(jour,day) == True:
                        s += 1
            else:
                if bissextile(year)== True:
                    for day in range(1,29+1):
                        today = datetime.date(year, month, day).weekday()
                        jour = int2day(today)
                    if magique(jour,day) == True:
                        s += 1
                else:
                    for day in range(1,28+1):
                        today = datetime.date(year, month, day).weekday()
                        jour = int2day(today)
                    if magique(jour,day) == True:
                        s += 1
    
print(nb_magique())
    