# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:17:08 2021

@author: Zacharie
"""

import wave

Son = wave.open('C:/Users/Zacharie/Desktop/PyDéfi/message1.wav','rb')
n = Son.getnframes()
print(Son.readframes(n))