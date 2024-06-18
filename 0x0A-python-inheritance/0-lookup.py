#!/usr/bin/python3
"""Contains the `lookup` function"""


def lookup(obj):
    """Returns the list of available attributes & methods of an object
    Args:
        obj: object to check
    Returns:
        list of available attributes and methods
    """
    my_list = dir(obj)
    return my_list
