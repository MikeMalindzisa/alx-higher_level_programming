#!/usr/bin/python3

class LockedClass:
    """
    A class that restricts the creation of instance attributes, allowing only 'first_name' to be set.
    
    Attributes:
        None

    Methods:
        __setattr__(self, attr, value):
            Overrides the default attribute setter method to control attribute creation.
            Raises an AttributeError if the attribute name is not 'first_name'.
    """

    def __setattr__(self, attr, value):
        """
        Override the default attribute setter method to control attribute creation.
        
        Args:
            attr (str): The name of the attribute to be set.
            value (any): The value to assign to the attribute.
        
        Raises:
            AttributeError: If the attribute name is not 'first_name'.
       """
        if attr != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(attr))
        super().__setattr__(attr, value)

