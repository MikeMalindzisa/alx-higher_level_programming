#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first 'x' elements from the given list.

    Args:
        my_list (list, optional): The list of elements. Defaults to an
        empty list.
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The actual number of elements printed.

    Notes:
        This function uses a try-except block to handle IndexError
        if 'x' is greater than the length of 'my_list'.
    """
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed += 1
    except IndexError:
        pass
    finally:
        print()
        return printed
