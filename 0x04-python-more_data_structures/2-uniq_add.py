#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list
    Args:
        my_list: list to work with
    Returns sum of integers
    """
    my_set = set(my_list)
    new_list = list(my_set)
    num = 0
    for i in new_list:
        num += i

    return num
