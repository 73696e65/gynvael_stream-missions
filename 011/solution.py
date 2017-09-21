#!/usr/bin/env python

from sys import stdout

secret = "4e5d4e92865a4e495a86494b5a5d49525261865f5758534d4a89".decode("hex")

for x in secret:
    stdout.write( chr(((ord(x) ^ 50 ^ 115) + 89) & 255) )
    
# huh, that actually worked!