#!/usr/bin/python3
def roman_to_int(s):
    if not isinstance(s, str) or not s:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum((r[s[i]], -r[s[i]])[r[s[i]] < r[s[i+1]]] for i in range(len(s) - 1)) + r[s[-1]]
