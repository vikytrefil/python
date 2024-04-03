#!/usr/bin/env python3

import bubblesort

morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
'y':'-.--', 'z':'--..', ' ':''}

def preloz():
    vstup = input('Zadej text:')

    for pismeno in vstup:
        try:
            print(morse[pismeno.lower()])
        except:
            print('?/', end ="")

if __name__== '__main__':
    preloz()
    pole= [9,4,5,7,1,3]
    print(bubblesort.simple(pole))
    