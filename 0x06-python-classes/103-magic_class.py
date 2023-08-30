#!/usr/bin/python3
import dis
import math

class _MagicClass__radius:
    def __init__(self, radius):
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius

magic_instance = _MagicClass__radius(5)

print("Disassembly of __init__:")
dis.dis(magic_instance.__init__)

print("\nDisassembly of area:")
dis.dis(magic_instance.area)

print("\nDisassembly of circumference:")
dis.dis(magic_instance.circumference)
