from libmicrocontest2_python27 import *
cont = commence_contest(16, "Zach4", " ")

chaine = cont.get_str("chaine")

def research(chaine):
    nb = ".0123456789"
    s = ""
    for x in chaine:
        if x in nb:
            s += x
    return float(s)

nombre = research(chaine)
cont.append_answer("nombre",nombre)

print(chaine)
print(nombre)
print(cont.submit_answer())

