from libmicrocontest2_python27 import *

cont = commence_contest(13, "Zach4", " ")

tab = cont.get_str("tableau")
ordre = cont.get_int("ordre")
L = []
for x in tab:
    L.append(ord(x))
if ordre == 0:
    L = sorted(L)
else:
    L = sorted(L)[::-1]
    
tab_c = ""
for x in L:
    tab_c += chr(x)
print(tab_c)
    
cont.append_answer("tableau_classe", tab_c)
print(cont.submit_answer())
