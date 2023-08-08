#!/usr/bin/python3
def uppercase(s):
    print(''.join("{:s}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z' else c for c in s))
