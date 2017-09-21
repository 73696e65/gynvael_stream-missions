#!/usr/bin/env python

from sys import stdout

# http://www.computer-engineering.org/ps2keyboard/scancodes2.html

scancodes = {
    "12": "[L SHFT]",
    "1b": "S",
    "1c": "A",
    "23": "D",
    "24": "E",
    "29": " ",
    "2c": "T",
    "2d": "R",
    "31": "N",
    "32": "B",
    "35": "Y",
    "41": ",",
    "43": "I",
    "44": "O",
    "49": ".",
    "4d": "P",
    "52": "'",
    "58": "[CAPS]",
    "59": "[R SHFT]",
    "42": "K",
}

secret = "58 f0 58 1b f0 1b 58 f0 58 44 f0 44 2d f0 2d 2d f0 2d 35 f0 35 41 f0 41 29 f0 29 59 43 f0 43 f0 59 29 f0 29 23 f0 23 44 f0 44 31 f0 31 52 f0 52 2c f0 2c 29 f0 29 1b f0 1b 4d f0 4d 24 f0 24 1c f0 1c 42 f0 42 29 f0 29 12 42 f0 42 f0 12 24 f0 24 35 f0 35 32 f0 32 44 f0 44 1c f0 1c 2d f0 2d 23 f0 23 49 f0 49"

codes = [secret[i:i+2] for i in range(0, len(secret), 9)]

print(''.join(map(lambda x: scancodes[x], codes))) 

"""
[CAPS]S[CAPS]ORRY, [R SHFT]I DON'T SPEAK [L SHFT]KEYBOARD.
Sorry, I don't speak Keyboard.
"""