#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at specific position
    without modifying the original list
    Args:
        my_list: the list to modify
        idx: position in list
        element: replacement value
    Returns a new modified list
    """
    new_list = my_list[:]

    if idx < 0:
        return new_list
    elif idx >= len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
