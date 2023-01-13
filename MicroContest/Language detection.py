from libmicrocontest2_python27 import *
from langdetect import detect

cont = commence_contest(37, "Zach4", " ")

 
txt1 = cont.get_str("txt1")    
txt2 = cont.get_str("txt2")
txt3 = cont.get_str("txt3")
txt4 = cont.get_str("txt4")  

print(txt1)
lang1 = detect(str(txt1))
lang2 = detect(str(txt2))
lang3 = detect(str(txt3))
lang4 = detect(str(txt4))
print(lang1)
print(txt2)
print(lang2)


cont.append_answer("lang1", lang1)
cont.append_answer("lang2", lang2)
cont.append_answer("lang3", lang3)
cont.append_answer("lang4", lang4)


print(cont.submit_answer())
