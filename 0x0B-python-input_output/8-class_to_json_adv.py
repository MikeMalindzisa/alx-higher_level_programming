#!/usr/bin/python3
"""
This module defines a function to serialize an object to a
dictionary with simple data structures.
"""


def class_to_json(obj):
    """
    Serialize an object to a dictionary with simple data structures.

    This function takes an object as input and returns a dictionary
    representation
    of the object by serializing its attributes that are of simple data types
    (list, dict, str, int, or bool).

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.
    """
    obj_dict = {}

    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)

        if isinstance(attr_value, (list, dict, str, int, bool)):
            obj_dict[attr_name] = attr_value

    return obj_dict
