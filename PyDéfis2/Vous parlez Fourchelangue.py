# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:44:37 2021

@author: Zacharie
"""

phrase = "FHSFHHSSFHSSHSHFFSSHFSFHSSSFHFHFSSFFFHHHSSFHHHHSSHHSSHFHSHFHHHHSSFHSSSHFSHHHSHSFFFSSFHSFSSFSFHFHSSFSHHHSHHHFHHFFFFSFHSHHFFHHFFFFSFHSSSFFHHFFFFSHHSSHSHFHFSFHSSSFFHHFFFFSHHSHFHFFSFFSFHHSSFFSHHSSSHSSFFHFHHHSSFHSHHFFHHFFFFFFFHHHHHFSFHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFHSSHHSSHHSSHSSSHFSHHSHHSFSFFHHHHHFSHHSHHHFSSSSFFHHFFHFFSSSHFSHHSHHSFSFHFHHHHHHSFSFSSHFSHHSSSHHHSHSFFSFHHFSFFSHSFFFFFSSHHSHHSHFFSSHFHHSHHHFHFSFSHHHSHFHFFSHFHFSHHHSFHHFSFHSSSHHHSHSSHSFHHFSFFHSHFHSHSHSSSFSSHHSSSFFHHFFFFSHHSFSSSSHSSFSSHFSFFHHSSFHHSHSHHFFFSFFFFSHHSSSFFHHFFFFSHHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFFHHSSFFSHHSSHHSSHFSHHSHFHFFFHHSFSFSSHFSH"
phrase2 = ""

def fourchelangue(ch):
    if ch == 'HFH':
        return 'A'
    if ch == 'FFH':
        return 'B'
    if ch == 'SHS':
        return 'C'
    if ch == 'SHH':
        return 'D'
    if ch == 'SSH':
        return 'E'
    if ch == 'FHF':
        return 'F'
    if ch == 'FSS':
        return 'G'
    if ch == 'HFF':
        return 'H'
    if ch == 'HHH':
        return 'I'
    if ch == 'SFS':
        return 'K'
    if ch == 'FFS':
        return 'L'
    if ch == 'FHS':
        return 'M'
    if ch == 'SSF':
        return 'N'
    if ch == 'FHH':
        return 'O'
    if ch == 'HHF':
        return 'P'
    if ch == 'SFF':
        return 'Q'
    if ch == 'FSF':
        return 'R'
    if ch == 'FSH':
        return 'S'
    if ch == 'HHS':
        return 'T'
    if ch == 'FFF':
        return 'U'
    if ch == 'SSS':
        return 'W'
    if ch == 'HFS':
        return 'X'
    if ch == 'SHF':
        return 'Y'
    if ch == 'SFH':
        return 'Z'

i = 0
while i < len(phrase):
    if phrase[i]+phrase[i+1]=="HS":
        phrase2 += " "
        i += 2
    else:
        a = phrase[i]+phrase[i+1]+phrase[i+2]
        phrase2 += fourchelangue(a)
        i += 3
    
print(phrase2)
