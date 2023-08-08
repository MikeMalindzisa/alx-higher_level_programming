#!/usr/bin/python3
for x in range(100):
    print("{:02}".format(x), end=", " if x < 99 else "\n")

