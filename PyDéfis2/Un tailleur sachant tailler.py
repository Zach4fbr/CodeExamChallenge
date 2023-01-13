# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:15:53 2021

@author: Zacharie
"""

marges = {10: 130, 13: 170, 21:277, 25:332, 27:361}
longueurs = [1465, 1009, 1461, 1737, 1224, 1562, 1052, 1772, 1512, 1396]
#longueurs = [33,23]
N = max(longueurs)+1
marges_max = [0]*N
for i in range(N):
    for lon in marges.keys():
        if i+lon < N:
            marges_max[i+lon] = max(marges_max[i+lon], marges_max[i] + marges[lon])
print(sum([marges_max[lon] for lon in longueurs]))
