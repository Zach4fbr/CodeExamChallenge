# -*- coding: cp1252 -*-
from libmicrocontest2_python27 import *
cont = commence_contest(11, "Zach4", " ")

import math
import sys
import urllib2

def get_probable_key(cipher, key_len):
    i = 0
    vigenere_key = ''
    while i < key_len:
        subcipher = sub_string(cipher, i, key_len)
        vigenere_key += frequency_cryptanalysis(subcipher)
        i += 1
    return vigenere_key


def vigenere_uncipher(ciphered, key):
    out_string = ''
    if ciphered != '' and key != '':
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')

        ord_key = []
        i = 0
        len_key = len(key)
        while i < len_key:
            ord_key.append(ord(key[i]) - A)
            i += 1

        i = 0
        l = len(ciphered)

        j = 0
        while i < l:
            ch_cipher = ord(ciphered[i])
            if ch_cipher >= a and ch_cipher <= z:  # lowercase
                ch_cipher -= ord_key[j % len_key]
                if ch_cipher < a:
                    ch_cipher += 26
                j += 1
            elif ch_cipher >= A and ch_cipher <= Z: # uppercase
                ch_cipher -= ord_key[j % len_key]
                if ch_cipher < A:
                    ch_cipher += 26
                j += 1
            out_string += chr(ch_cipher)

            i += 1

    return out_string


def get_probable_key_length(cipher):
    french_ic = 0.074
    min_diff = 1
    gap = 0.01
    key_len = 2

    keys_lengthes = []

    number_of_acceptable_ic = 0
    max_number_of_acceptable_ic = 0
    i = 2
    while i <= 10:
        ics = coincident_index_with_step(cipher, i)
        number_of_acceptable_ic = 0
        for ic in ics:
            if math.fabs(float(ic) - french_ic) < gap:
                number_of_acceptable_ic += 1

        if math.fabs(float(ic) - french_ic) < gap:
            max_number_of_acceptable_ic = number_of_acceptable_ic
            key_len = i

            addit = 1

            if addit:
                keys_lengthes.append(key_len)
                key_len = i

        i += 1
    return key_len


def coincident_index(cipher):
    tot_ic = 0.0

    ch = ord('A')
    i = 0
    n = len(cipher)
    while i < 26:
        ni = cipher.count(chr(ch))
        ic = float(ni * (ni - 1)) / (n * (n - 1))
        tot_ic += ic

        i += 1
        ch += 1
    return tot_ic


def coincident_index_count(
    cipher,
    letter,
    start,
    step,
    ):
    c = 0
    d = 0
    i = start
    l = len(cipher)

    while i < l:
        if cipher[i] == letter:
            c += 1
        d += 1
        i += step
    return (c, d)


def frequency_cryptanalysis(cipher):
    occs = {}
    i = 0
    l = len(cipher)
    while i < l:
        if occs.has_key(cipher[i]):
            occs[cipher[i]] += 1
        else:
            occs[cipher[i]] = 1
        i += 1
    letter = ''
    max = -1
    for key in occs.keys():
        if occs[key] > max:
            max = occs[key]
            letter = key

    E = ord('E')
    ciphered_letter = ord(letter)

    diff = ciphered_letter - E
    if diff < 0:
        diff += 26
    return chr(ord('A') + diff)


def sub_string(cipher, start, step):
    out = ''
    i = start
    l = len(cipher)
    while i < l:
        out += cipher[i]
        i += step
    return out


def coincident_index_with_step(cipher, step):
    indexes = []
    start = 0
    while start < step:

        ch = ord('A')
        i = 0
        tot_ic = 0.0
        while i < 26:
            (ni, n) = coincident_index_count(cipher, chr(ch), start,
                    step)
            if n != 0 and n - 1 != 0:
                ic = float(ni * (ni - 1)) / (n * (n - 1))
                tot_ic += ic

            i += 1
            ch += 1
        indexes.append(tot_ic)
        start += 1
    return indexes


def avg(l):
    sum = 0
    for i in l:
        sum += i
    return sum / len(l)

texte = cont.get_str('txt_crypte')
cipher = texte  # TODO: Fill this var with relevant data
cipher_tmp = cipher.replace(' ', '')
key_len = get_probable_key_length(cipher_tmp)
probable_key = get_probable_key(cipher_tmp, key_len)
txt_plain = vigenere_uncipher(cipher, probable_key)
print(txt_plain)

    
cont.append_answer("txt_clair", txt_plain)
print(cont.submit_answer())
