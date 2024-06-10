#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list
    Args:
        my_list: list to work with
    Returns list with bool True if is, False if not
    """
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
