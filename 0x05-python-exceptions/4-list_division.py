#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and
    returns a new list
    with the divisions.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of
        the resulting list.

    Returns:
        list: A new list containing the
        division results.
    """
    result = []

    for i in range(list_length):
        try:
            div = 0
            try:
                element1 = my_list_1[i]
            except IndexError:
                print("out of range")
                element1 = 1

            try:
                element2 = my_list_2[i]
            except IndexError:
                print("out of range")
                element2 = 1

            try:
                div = element1 / element2
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            finally:
                result.append(div)

        except (IndexError, ZeroDivisionError, TypeError):
            result.append(0)

    return result
