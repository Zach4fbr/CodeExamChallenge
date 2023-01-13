# -*- coding: cp1252 -*-

from libmicrocontest2_python27 import *
cont = commence_contest(3, "Zach4", " ")

t = cont.get_str("texte")
m = cont.get_str("mot")


def occurences(ch,mot):
    s = 0
    virgule = mot+","
    s += ch.count(virgule)
    espace = mot+" "
    s += ch.count(espace)
    point = mot+"."
    s += ch.count(point)
    return s

occ = occurences(t,m)
print(occ)

cont.append_answer("occ", occ)
print(cont.submit_answer())
