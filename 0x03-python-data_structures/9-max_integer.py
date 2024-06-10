#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list
    Args:
        my_list: list to work with
    Returns biggest number
    """
    if len(my_list) == 0:
        return None

    prev = my_list[0]
    for num in my_list:
        if num > prev:
            prev = num

    return prev
