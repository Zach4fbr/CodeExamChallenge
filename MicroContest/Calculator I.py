from libmicrocontest2_python27 import *
from sympy import *

cont = commence_contest(19, "Zach4", " ")
 
str_expr = cont.get_str("expr")
expr = sympify(str_expr)

res = float(expr)
res = round(res,0)

print(res)

cont.append_answer("result", res)
print(cont.submit_answer())
