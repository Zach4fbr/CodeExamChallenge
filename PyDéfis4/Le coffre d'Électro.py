# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:36:18 2021

@author: Zacharie
"""

import urllib.request
import re

def search(text):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    urls = re.findall(regex, text) 
    n = len(urls)
    return urls,n

T = []
txt = urllib.request.urlopen("https://pydefis.callicode.fr/defis/UrlElectro/intern/code/03fCF23cfE").read()
txt = str(txt)
T.append(txt)

 

for i in range(1,200):
    if search(txt)[1] != 1:
        url = search(txt)[0][1][0]
        T.append(url)
        txt = urllib.request.urlopen(url).read()
        txt = str(txt)
    else:
        url = search(txt)[0][0][0]
        T.append(url)
        txt = urllib.request.urlopen(url).read()
        txt = str(txt)
        
#Bravo le code du coffre est : 9531
