from libmicrocontest2_python27 import *

cont = commence_contest(15, "Zach4", " 
 
x = cont.get_int("x")
import urllib
import re

def isNumber(car):
    numb = "0123456789"
    for x in numb:
        if x == car:
            return True
        

link = "http://www.microcontest.com/contests/15/contest.php"
f = urllib.urlopen(link)
myfile = f.read()

myfile = str(myfile[::])
print(myfile)


rep = "?x="
rep += myfile[38]+myfile[39]
print("rep=",rep)

link = link + rep
print(link)

f = urllib.urlopen(link)
myfile = f.read()

myfile = str(myfile[::])
print(myfile)

m = re.search('<p>(.+?)</p>', myfile)
if m:
    found = m.group(1)
print("y =",found)



cont.append_answer("y", found)
print(cont.submit_answer())
