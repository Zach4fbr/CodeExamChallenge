import numpy as np
from libmicrocontest2_python27 import *

cont = commence_contest(8, "Zach4", " ")

h = cont.get_int("h")
H = cont.get_int("H")
D = cont.get_int("D")
v0 = cont.get_int("v0")
theta = cont.get_float("theta")
g = 9.81

def y(t):
    return -g*t**2/2 + v0*np.sin(theta)*t + h

T = D/(v0*np.cos(theta))
e = y(T)-H
print(T,e)



     
cont.append_answer("e", e)
cont.append_answer("duree", T)
print(cont.submit_answer())
