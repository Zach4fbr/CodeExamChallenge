from libmicrocontest2_python27 import *

cont = commence_contest(42, "Zach4", " ")
 
s1 = cont.get_str("s1")    
s2 = cont.get_str("s2")
s3 = s1+s2
cont.append_answer("s3", s3)
print(cont.submit_answer())
