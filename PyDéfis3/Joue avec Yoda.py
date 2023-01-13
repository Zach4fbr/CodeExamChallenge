# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:29:45 2020

@author: Zacharie
"""


chc = "sassai eaux-de-vie cessaient acerbité eaux sceau tiendra hasard acéphale auxiliairement vesce eurafricaine hâtai saignant entachassent alentie césar vieillerie messéant taillable ives testacé dracéna ardentes ensablant blessas entachasses ioniens antarctique sessiles ineffaçables quercitrine besace lessivasses acerbes descellaient entachas lessive gestation lessivâtes antécédentes énamourâmes antécédent entachât inefficace testacelles sarabandes entachant rieur itérâmes antécédences messages sesquioxydes testacés"
chc = chc.split(" ")

B = ["acerbité","itérâmes","messages"]

def NextMots(mot,R):
    a = mot[-3:]
    L = []
    for i in range(len(R)):
        r = R[i][:3]
        if r == a:
            L.append(R[i])
    return L


def Possibilities(R,B):
    if len(R)==1:
        return [R[0]]
    else:
        L = []
        for nex in NextMots(B[-1],R):
            C = R[:].remove(nex)
            D = B[:].append(nex)
            for pos in Possibilities(C,D):
                L.append(pos)
        if len(L)==0:
            return B
        return L
    


R = [x  for x in chc  if x not in B]
#print(NextMot(chc[0],R))

"""for i in range(2,len(chc)):
    N = NextMots(B[i],R)
    print(N)
    nex = N[0]
    B.append(nex)
    R.remove(nex)

print(B)"""

print(Possibilities(R,B))
        
#print(NextMot(B[1],chc))