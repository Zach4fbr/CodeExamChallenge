from libmicrocontest2_python27 import *
cont = commence_contest(10, "Zach4", " ")

def code_vigenere ( message, cle, decode = False) :
    message_code = ""
    for i,c in enumerate(message) :
      if message[i] == ' ':
          message_code += ' '
      else:
          d = cle[ i % len(cle) ]
          d = ord(d) - 65
          if decode : d = 26 - d
          message_code += chr((ord(c)-65+d)%26+65)
    return message_code

def DecodeVigenere(message, cle):
    return code_vigenere(message, cle, True)


txt_crypte = cont.get_str('txt_crypte')
clef = cont.get_str('clef')
n = len(clef)
clef = clef*(len(txt_crypte)//n -1)

clef2 = ""
s = 0
for i in range(len(txt_crypte)):
    if txt_crypte[i] == ' ':
        clef2 += ' '
        s += 1
    else:
        clef2 += clef[i-s]

txt_clair = DecodeVigenere(txt_crypte, clef2)

print(txt_clair)

cont.append_answer("txt_clair", txt_clair)
print(cont.submit_answer())
