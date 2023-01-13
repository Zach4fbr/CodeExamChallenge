# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:07:28 2021

@author: cypri
"""

import calendar
 
year = 2005
month = 12
 
 
obj = calendar.Calendar()
 
# iterating with itermonthdays
"""
for day in obj.itermonthdays2(year, month):
    print("")
""" 
    
    
jour = [5,5,8,5,8,6,8]
nb = 0

for year in range(2000,2022):

    for months in range(1,13):
        for day in obj.itermonthdays2(year, month):
            if not ((year == 2021 and months > 9) or (year == 2021 and months == 9 and day[0]>28)): #mettre ici le jour actuel
                if day[0] != 0:
                    if (day[0]+jour[day[1]]) % 10 == 0:
                        nb += 1
