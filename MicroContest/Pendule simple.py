import numpy as np
from libmicrocontest2_python27 import *

cont = commence_contest(51, "Zach4", " ")

g = 9.81
l = cont.get_float("l")
theta_0 = cont.get_float("theta_0")

w0 = np.sqrt(g/l)

t = np.arange(1,11)

a = theta_0*2*np.pi/360

theta= []
theta_p = []
theta_pp = []

for i in range(len(t)):
    theta.append(a*np.cos(w0*t[i]))
    theta_p.append(-w0*a*np.sin(w0*t[i]))
    theta_pp.append(-w0**2*a*np.cos(w0*t[i]))
    
def truncate(x, d):
    return int(x*(10.0**d))/(10.0**d)

strtheta = ""
strtheta_p = ""
strtheta_pp = ""
for i in range(len(theta)):
    theta[i] = truncate(theta[i],5)
    theta_p[i] = truncate(theta_p[i],5)
    theta_pp[i] = truncate(theta_pp[i],5)
    strtheta += str(theta[i])+";"
    strtheta_p += str(theta_p[i])+";"
    strtheta_pp += str(theta_pp[i])+";"
 
n = len(strtheta)    
strtheta = strtheta[:n-1]
n = len(strtheta_p)    
strtheta_p = strtheta_p[:n-1]
n = len(strtheta_pp)    
strtheta_pp = strtheta_pp[:n-1]

cont.append_answer("theta", strtheta)
cont.append_answer("dtheta", strtheta_p)
cont.append_answer("ddtheta", strtheta_pp)
print(cont.submit_answer())


    
