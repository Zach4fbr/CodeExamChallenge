# -*- coding: cp1252 -*-
import base64
from libmicrocontest2_python27 import *
cont = commence_contest(50, "Zach4", " ")

original_string = cont.get_str("big_number")   

#original_string = 'MTU2ODE3ODM2Ng=='
print('Original:', original_string)

decoded_string = base64.b64decode(original_string)
print('Decoded :', decoded_string)

decoded_string = str(int(decoded_string)/2)
print("Intermediaire :", decoded_string)
encoded_string = base64.b64encode(decoded_string)
print('Encoded :', encoded_string)

half = encoded_string

cont.append_answer("half_big_number", half)
print(cont.submit_answer())
