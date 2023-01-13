from libmicrocontest2_python27 import *

cont = commence_contest(14, "Zach4", " ")
 
naissance = cont.get_int("naissance")
date_courante = cont.get_int("date_courante")
 
age = date_courante - naissance
 
# then append the answer
cont.append_answer("age", age)
# then submit the answer and print result
print(cont.submit_answer())

