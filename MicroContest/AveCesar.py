# -*- coding: utf-8 -*-
from libmicrocontest2_python27 import *
 
if not check_version():
    print "Warning: the version of the libmicrocontest2 is not the last one."
    print "Current version :\t" + get_currentversion()
    print "This program may not work properly. Consider downloading the latest version on\nthis page : http://www.microcontest.com/download.php\n"  
 
cont = commence_contest(4, "Zach4", " ")
# short form uses username, password from credentials.py
# cont = commence_contest(1)
 
CryptedText = cont.get_str('txt_crypte')
Key = cont.get_int('key')
PlainText = ''
 
for c in CryptedText:
    NewChar = ord(c) - Key
    if NewChar < 65:
        NewChar += 26
    PlainText += chr(NewChar)
 
print 'CryptedText:\t' + CryptedText
print 'Key:\t\t' + str(Key)
print 'PlainText:\t' + PlainText
 
cont.append_answer("txt_clair", PlainText)
print(cont.submit_answer())
