#!/usr/bin/env python

from sys import stdout
from pwn import *

target = ("31.133.0.131", 9393)

def determine_length():
    for i in range(1, 5000):
        stdout.write("Trying {0}\n".format(i))
        x = remote(*target)

        stdout.write(x.recvuntil("Enter shared secret mask you want to try:\n"))
        x.sendline("1" * i)
        result = x.recvline()
        x.close()

        if "Mask too short. Bye." not in result:
            stdout.write("Found length: {0}\n".format(i))
            return i

def part_1(length):
    x = remote(*target)
    stdout.write(x.recvuntil("Enter shared secret mask you want to try:\n"))

    mask = "00000001" * (length // 8)
    x.sendline(mask)
    stdout.write(x.recvuntil("Alright, now send in the bits:\n"))

    bits = "0" * (length // 8)
    x.sendline(bits)
    stdout.write(x.recvuntil("End of messages.\n"))
    x.close()

def part_2(length):
    guessed = str()
    mask_padding = "00000001" * (length // 8)

    for i in range(1, length+1):
        x = remote(*target)
        mask = "1" * i + mask_padding[i:]
        x.sendline(mask)
        secret = guessed + "1" + "0" * ((length // 8) - (i // 8)) 
        x.sendline(secret)
        for _ in range(3): answer = x.recvline()
        x.close()

        guessed += "1" if "Access Granted" in answer else "0"

    guessed = guessed[::-1]
    solution = ''.join( (map(lambda x: chr(int(x, 2)), [guessed[i:i+8] for i in range(0, len(guessed), 8)])) )[::-1]
    stdout.write( solution + "\n" )

length = determine_length() # 560
pause()

part_1(length) # Just Another Secret Message
pause()

part_2(length) # This Crypto Is Absolutely Secure And There Will Be No Problem With It.