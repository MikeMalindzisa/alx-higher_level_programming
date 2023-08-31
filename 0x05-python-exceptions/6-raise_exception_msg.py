#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raises a name exception with a provided message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
