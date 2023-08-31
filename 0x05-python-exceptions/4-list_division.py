#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and returns a new list
    with the divisions.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list containing the division results.
    """
    result = []

    for i in range(list_length):
        try:
            div = 0
            if i < len(my_list_1) and i < len(my_list_2):
                element1 = my_list_1[i]
                element2 = my_list_2[i]

                if isinstance(element1, (int, float)) and \
                   isinstance(element2, (int, float)):
                    if element2 != 0:
                        div = element1 / element2
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
            result.append(div)
        except (IndexError, ZeroDivisionError):
            result.append(0)
        except TypeError:
            print("wrong type")

    return result
