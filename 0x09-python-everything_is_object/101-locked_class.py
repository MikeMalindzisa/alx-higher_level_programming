#!/usr/bin/python3
"""
Defines a locked class, LockedClass.

This class restricts the creation of instance attributes to only one attribute, 'first_name'. 
It uses the __slots__ mechanism to achieve this restriction, preventing users from dynamically 
creating new attributes beyond 'first_name'.

Attributes:
    None
Methods:
    None
"""


class LockedClass:
    """
    A class that restricts the creation of instance attributes, allowing only 'first_name' to be set.

    Attributes:
        None
    Methods:
        None
    """
    __slots__ = ["first_name"]
                                                        
