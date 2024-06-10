#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: the list to work on
        idx: element position to replace
        element: element to work with

    The return value is new list
    """
    if idx < 0:
        return my_list
    elif idx > len(my_list) + 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
