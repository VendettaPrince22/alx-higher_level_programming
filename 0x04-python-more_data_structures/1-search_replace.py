#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list
    Args:
        my_list: list to work with
        search: element to replace
        replace: new element
    Returns a new list
    """
    new_list = list(map(lambda x: 89 if x == search else x, my_list))

    return new_list
