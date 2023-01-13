from libmicrocontest2_python27 import *
import numpy as np

cont = commence_contest(12, "Zach4", " ")
 
A = cont.get_str("A")
B = cont.get_str("B")

def matrix(A):
    R = ""
    for i in range(len(A)-1):
        if A[i] == ']' and A[i+1] == '[':
            R += A[i]
            R += ','
        else:
            R += A[i]
    R += ']'
    return R

def string(M):
    R = '['
    for i in range(len(M)):
        R += str(M[i])
    R += ']'
    A = R.replace('[ ','[')
    B = A.replace(' ',',')
    C = B.replace(',,',',')
    D = C.replace(',]',']')
    E = D.replace(',,',',')
    return E
            
A = eval(matrix(A))
B = eval(matrix(B))
T = np.transpose(B)
A = np.array(A)
T = np.array(T)
C = np.dot(A,T)
M = np.linalg.inv(C)
M = string(M)
print(M,type(M))

#A = "[[13,2,5,23][-2,0,1,3][-1,3,7,77]]"
#B = "[[13,-2,1,7][2,3,3,77][99,13,0,777]]"


cont.append_answer("M", M)
print(cont.submit_answer())
