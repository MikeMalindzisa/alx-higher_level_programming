#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists and returns a new list with
    results.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The length of the new list to be returned.

    Returns:
        list: A new list with division results.
    """
    result = []
    for i in range(list_length):
        try:
            num_1 = my_list_1[i] if i < len(my_list_1) else 0
            num_2 = my_list_2[i] if i < len(my_list_2) else 0

            if (isinstance(num_1, (int, float)) and
                    isinstance(num_2, (int, float))):
                if num_2 != 0:
                    result.append(num_1 / num_2)
                else:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
    return result
