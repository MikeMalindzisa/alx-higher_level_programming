#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add as addition
    print("{} + {} = {}".format(a, b, addition(a, b)))
