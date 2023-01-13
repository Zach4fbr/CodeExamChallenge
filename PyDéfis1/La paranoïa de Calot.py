# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:15:14 2020

@author: Zacharie
"""

ch1 = "azertyuiop"
ch2 = "qsdfghjklm"
ch3 = "wxcvbn,;:!"

chc = "hok:sopkhopgue;du:jeuploahtegrxropcdoyptytkojeoxtekxtekpoapte!rtxkluxkexyoarapokauepuxaltxagokyguakxoktxayukmpux:sohoxawtxkhurkjerugu!uxauqolowpterggopgokyrkaoklokohytrktxxoepkuhokaptekkokvytephopoapte!opoxyupauxalewepoueuggoiatealptracatepxoiuque:socatepxoiuque:socatepxoiulptraocuggoiatealptracyr!taoikep!tekhohocpoxapoiluxkgoyup:cuppr!ougumtxaurxocohypexaoigoguwzprxaso!oqoaugcmtx:oiatealptrau::pteyrkytepoxapopluxkgokatrgoaaokyewgrjeokcuemtxlulptrao!tekapte!opoiexoytpaolokop!r:ojerltxxolrpo:aohoxau::okue;:erkrxoklepokauepuxacgo:tloloxapoookajeupuxaoloe;:rxjeuxaoseralrokocuaaoxartxoxte!puxaguytpaodurytkrartxxoexkouelu:rlokyo:rugohoxarhytpaoleyup:zoggt,katxodekaouelokkeknn:ogukopuralthhuqojeo!tekktzoilrkktekdekaou!uxalohopoapte!opnjeuxlgo:erkrxrop!teklohuxlopu:ojeo!tek!tegoihuxqoplraokgerblok:tpxr:stxkue!rxurqpooaleqtgtewakzcrg!tek:txlerpuauhuauwgon"
exemple = "zavqapxutmutxutmmoxap"


def DansQuelleChaine(x):
    for j in ch1:
        if x == j:
            return 1
    for j in ch2:
        if x == j:
            return 2
    for j in ch3:
        if x == j:
            return 3
    
def PositionChaine(x,L):
    for i in range(len(L)):
        if L[i] == x:
            return i

def Decalage(n,L):
    c = ""
    for i in range(len(L)):
        z = int(L[i])+n
        if z >= 10:
            z = z - 10
        elif z < 0:
            z = z + 10
        c += str(z)
    return c

def Decodage(a,c):
    d = ""
    for i in range(len(a)):
        if a[i] == '1':
            d += ch1[int(c[i])]
        if a[i] == '2':
            d += ch2[int(c[i])]
        if a[i] == '3':
            d += ch3[int(c[i])]
    return d


exemple = chc
for n in range(-9,10):
    
    a = ""
    b = ""
    c = ""
    
    for i in range(len(exemple)):
        a += str(DansQuelleChaine(exemple[i]))
        if a[i] == '1':
            b += str(PositionChaine(exemple[i],ch1))
        if a[i] == '2':
            b += str(PositionChaine(exemple[i],ch2))
        if a[i] == '3':
            b += str(PositionChaine(exemple[i],ch3))
    
    c = Decalage(n,b)
        
    print(Decodage(a,c))
    print("")



