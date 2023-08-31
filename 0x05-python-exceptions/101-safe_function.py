#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Executes a function safely and returns its result.

    Args:
        fct (function): The function to be executed.
        *args: Arguments to be passed to the function.

    Returns:
        The result of the function. Returns None and prints the exception to
        stderr if an error occurs during execution.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
