from libmicrocontest2_python27 import *
import time

cont = commence_contest(18, "Zach4", " ")
 
#d = cont.get_str("date")

t = int(time.time())


# then append the answer
cont.append_answer("timestamp", t)

# then submit the answer and print result
print(cont.submit_answer())
