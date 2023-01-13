from libmicrocontest2_python27 import *

cont = commence_contest(43, "Zach4", " ")
 
s = cont.get_str("s")    
cont.append_answer("s_rev", s[::-1])
print(cont.submit_answer())
