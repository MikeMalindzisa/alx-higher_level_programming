#!/usr/bin/python3
import string; (lambda s: [__import__('sys').stdout.write(s[i]) for i in range(len(s))])(string.ascii_uppercase + '\n')
