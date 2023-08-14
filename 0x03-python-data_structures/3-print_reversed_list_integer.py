#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_integers = reversed([n for n in my_list if isinstance(n, int)])
    formatted_strings = map("{:d}".format, reversed_integers)
    print("\n".join(formatted_strings))
