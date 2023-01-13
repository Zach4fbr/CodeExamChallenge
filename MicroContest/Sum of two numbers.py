from libmicrocontest2_python27 import *

cont = commence_contest(1, "Zach4", " ")
# short form uses username, password from credentials.py
# cont = commence_contest(1)
 
a = int(cont.get_param("a", int))
# you can also use get_int, get_float, get_str
b = cont.get_int("b")
# or use it that way (it tries to return the right type automagically)
# s = cont.a + cont.b
 
s = a + b
 
# then append the answer
cont.append_answer("s", s)
# then submit the answer and print result
print(cont.submit_answer())
#or pass tuples directly to submit_answer (here using the short version)
#print cont.submit_answer([("s", cont.a + cont.b)])

