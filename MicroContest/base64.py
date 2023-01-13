#! /usr/bin/env python

"""RFC 3548: Base16, Base32, Base64 Data Encodings"""

# Modified 04-Oct-1995 by Jack Jansen to use binascii module
# Modified 30-Dec-2003 by Barry Warsaw to add full RFC 3548 support

import re
import struct
import binascii


__all__ = [
    # Legacy interface exports traditional RFC 1521 Base64 encodings
    'encode', 'decode', 'encodestring', 'decodestring',
    # Generalized interface for other encodings
    'b64encode', 'b64decode', 'b32encode', 'b32decode',
    'b16encode', 'b16decode',
    # Standard Base64 encoding
    'standard_b64encode', 'standard_b64decode',
    # Some common Base64 alternatives.  As referenced by RFC 3458, see thread
    # starting at:
    #
    # http://zgp.org/pipermail/p2p-hackers/2001-September/000316.html
    'urlsafe_b64encode', 'urlsafe_b64decode',
    ]

_translation = [chr(_x) for _x in range(256)]
EMPTYSTRING = ''


def _translate(s, altchars):
    translation = _translation[:]
    for k, v in altchars.items():
        translation[ord(k)] = v
    return s.translate(''.join(translation))




# Base64 encoding/decoding uses binascii

def b64encode(s, altchars=None):
    """Encode a string using Base64.
    s is the string to encode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    The encoded string is returned.
    """
    # Strip off the trailing newline
    encoded = binascii.b2a_base64(s)[:-1]
    if altchars is not None:
        return _translate(encoded, {'+': altchars[0], '/': altchars[1]})
    return encoded


def b64decode(s, altchars=None):
    """Decode a Base64 encoded string.
    s is the string to decode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies the
    alternative alphabet used instead of the '+' and '/' characters.
    The decoded string is returned.  A TypeError is raised if s were
    incorrectly padded or if there are non-alphabet characters present in the
    string.
    """
    if altchars is not None:
        s = _translate(s, {altchars[0]: '+', altchars[1]: '/'})
    try:
        return binascii.a2b_base64(s)
    except binascii.Error:
        # Transform this exception for consistency
        pass
        #raise TypeError(msg)


def standard_b64encode(s):
    """Encode a string using the standard Base64 alphabet.
    s is the string to encode.  The encoded string is returned.
    """
    return b64encode(s)

def standard_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.
    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.
    """
    return b64decode(s)

def urlsafe_b64encode(s):
    """Encode a string using a url-safe Base64 alphabet.
    s is the string to encode.  The encoded string is returned.  The alphabet
    uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64encode(s, '-_')

def urlsafe_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.
    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.
    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64decode(s, '-_')




# Legacy interface.  This code could be cleaned up since I don't believe
# binascii has any line length limitations.  It just doesn't seem worth it
# though.

MAXLINESIZE = 76 # Excluding the CRLF
MAXBINSIZE = (MAXLINESIZE//4)*3

def encode(input, output):
    """Encode a file."""
    while True:
        s = input.read(MAXBINSIZE)
        if not s:
            break
        while len(s) < MAXBINSIZE:
            ns = input.read(MAXBINSIZE-len(s))
            if not ns:
                break
            s += ns
        line = binascii.b2a_base64(s)
        output.write(line)


def decode(input, output):
    """Decode a file."""
    while True:
        line = input.readline()
        if not line:
            break
        s = binascii.a2b_base64(line)
        output.write(s)


def encodestring(s):
    """Encode a string into multiple lines of base-64 data."""
    pieces = []
    for i in range(0, len(s), MAXBINSIZE):
        chunk = s[i : i + MAXBINSIZE]
        pieces.append(binascii.b2a_base64(chunk))
    return "".join(pieces)


def decodestring(s):
    """Decode a string."""
    return binascii.a2b_base64(s)




# Useable as a script...
def test():
    """Small test program"""
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'deut')
    except getopt.error:
        sys.stdout = sys.stderr
        #print(msg)
        print("""usage: %s [-d|-e|-u|-t] [file|-]
        -d, -u: decode
        -e: encode (default)
        -t: encode and decode string 'Aladdin:open sesame'"""%sys.argv[0])
        sys.exit(2)
    func = encode
    for o, a in opts:
        if o == '-e': func = encode
        if o == '-d': func = decode
        if o == '-u': func = decode
        if o == '-t': test1(); return
    if args and args[0] != '-':
        with open(args[0], 'rb') as f:
            func(f, sys.stdout)
    else:
        func(sys.stdin, sys.stdout)


def test1():
    s0 = "Aladdin:open sesame"
    s1 = encodestring(s0)
    s2 = decodestring(s1)
    print(s0, repr(s1), s2)


if __name__ == '__main__':
    test()