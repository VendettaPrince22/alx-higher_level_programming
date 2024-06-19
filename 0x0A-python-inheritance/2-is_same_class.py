#!/usr/bin/python3
"""Contains the `is_same_class` function"""


def is_same_class(obj, a_class):
    """Returns bool if the object is / not instance of specified class
    Args:
        obj: object to check if instance
        a_class: class to check by
    Returns:
        bool; True if isinstance otherwise false
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
