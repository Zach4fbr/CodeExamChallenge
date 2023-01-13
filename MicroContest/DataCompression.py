from libmicrocontest2_python27 import *

cont = commence_contest(31, "Zach4", " 
 
comp = cont.get_str("donnees_a_compresser")    
decomp = cont.get_str("donnees_a_decompresser")

def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + str(cnt) + s[i - 1]
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + str(cnt) + s[i - 1]
    
    return r
               
import re
def decode(encoded):
    """
    Run-length encoding (RLE), decode the encoded input to the repeating values
    
    :param encoded: RLE encoded string
    :return: decoded string
    """
    output = ''
    encoded = re.sub(r'[^A-Za-z0-9 ]', '', encoded)
    groups = filter(None, re.split(r'([0-9]+[A-Za-z ]{1}|[A-Za-z ]{1})', encoded))
    for item in groups:
        if len(item) > 1:
            count, letter = re.search(r'([0-9]+)([A-Za-z ]+)', item).groups()
            output += str(letter) * int(count)
        else:
            output += item
    return output

print(comp)
a = compress(comp)
print(a)
print(decomp)
b = decode(decomp)
print(b)

cont.append_answer("resultat_compression", a)
cont.append_answer("resultat_decompression", b)
print(cont.submit_answer())

