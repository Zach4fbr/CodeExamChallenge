# -*- coding: cp1252 -*-
from libmicrocontest2_python27 import *
cont = commence_contest(5, "Zach4", " ")

def decode(texte, decalage):
    """Renvoie une chaine de caract�res d�cal�s
 
        Attend une cha�ne de caract�res non accentu�s
        �ventuellement vide : texte
 
        Un entier positif entre 0 et 25 : decalage
         
        Renvoie une cha�ne de la m�me longueur avec des caract�res
        d�cal�s de ... decalage, et ramen�s dans l'alphabet
        en revenant de 26si on d�passe z ou Z
 
        Garde les caract�res non alphab�tiques
    """
         
    # Une cha�ne vide � compl�ter au fur et � mesure
    resultat = ""
 
    # On parcourt la cha�ne texte
    for lettre in texte :
 
        # d�calage -> new est un code ASCII
        new = ord(lettre) + decalage
         
        if 65 <= ord(lettre) <= 90 :    # si minuscule
            if new > 90 :               # d�passement du z ?
                new -= 26
            resultat += chr(new)        # on rajoute le caract�re d�cal�
        elif 97 <= ord(lettre) <= 122 : # si majuscule
            if new > 122 :              # d�passement du Z ?
                new -= 26
            resultat += chr(new)        # on rajoute le caract�re d�cal�
        else :
            resultat += lettre   # on rajoute le caract�re non d�cal�
 
    # On renvoie la nouvelle cha�ne
    return resultat
# Des tests !
assert decode("", 5) == ""
assert decode("Ac Z!", 5) == "Fh E!"
 
###################################################################
 
# D�codage de ce mot :
 
mot = "XRLTYVJLIDFEKVUVGZXEFEJTFEWLJULEVMZJZFEUVMZCCRXVRLO"
mot2 = "GPVFUMFTKBNCFTSBJEJFTQBSEFTSIVNBUJTNFTUBOEJTRVFMF"
mot3 = "JCVPXAAPGSGDJMTITUUAPCFJTCTHTEGTHHPXIVJTGTETHPXIHJGAT"

mot = cont.get_str('txt_crypte1')
mot2 = cont.get_str('txt_crypte2')
mot3 = cont.get_str('txt_crypte3')


def occurence_e(mot):
    s = 0
    for x in mot:
        if x == "E" or x == "A":
            s += 1
    return s

L = []
L2 = []
L3 = []
for d in range(1,26):
    clair = decode(mot, d)
    clair2 = decode(mot2,d)
    clair3 = decode(mot3,d)
    O = occurence_e(clair)
    O2 = occurence_e(clair2)
    O3 = occurence_e(clair3)
    L.append((O,clair))
    L2.append((O2,clair2))
    L3.append((O3,clair3))

print(max(L)[1])
print(max(L2)[1])
print(max(L3)[1])
clair = max(L)[1]
clair2 = max(L2)[1]
clair3 = max(L3)[1]


cont.append_answer("txt_clair1", clair)
cont.append_answer("txt_clair2", clair2)
cont.append_answer("txt_clair3", clair3)
print(cont.submit_answer())



