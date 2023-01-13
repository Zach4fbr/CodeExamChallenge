from libmicrocontest2_python27 import *

cont = commence_contest(2, "Zach4", " ")
 
a = cont.get_float("a")
b = cont.get_float("b")
c = cont.get_float("c")

delta = b**2-4*a*c

x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)


# then append the answer
cont.append_answer("x1", x1)
cont.append_answer("x2", x2)

# then submit the answer and print result
print(cont.submit_answer())
