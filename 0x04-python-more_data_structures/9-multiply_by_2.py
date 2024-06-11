#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2
    Args:
        a_dictionary: dictionary to work with
    Returns a new dictionary
    """
    new_dictionary = {x: a_dictionary[x] * 2 for x in list(a_dictionary)}

    return new_dictionary
