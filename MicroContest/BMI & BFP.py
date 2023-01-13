from libmicrocontest2_python27 import *

cont = commence_contest(53, "Zach4", " 
 
M = cont.get_int("mass")    #en kg
H = cont.get_int("height")  #en cm
s = cont.get_int("sex")     #0 pour Male
age = cont.get_int("age")   #age

H = H/100.0
bmi = M/(H*H)
bfp = (1.2*bmi) + (0.23*age)-(10.8*s) - 5.4

print(bmi)
print(bfp)

cont.append_answer("bmi", bmi)
cont.append_answer("bfp", bfp)
print(cont.submit_answer())
