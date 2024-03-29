#!/usr/bin/python3
"""
This module defines a Student class to represent student objects.
"""


class Student:
    """
    Represents a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary.
                If None, include all attributes.

        Returns:
            dict: A dictionary containing the specified student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a
        dictionary representation.

        Args:
            json (dict): A dictionary containing attribute names
            and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
