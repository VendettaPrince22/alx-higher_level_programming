#!/usr/bin/python3
"""Contains the `is_kind_of_class` function"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of base class & derived class
    Args:
        obj: object to check
        a_class: class to check with
    Return:
        bool; True if is instance, False otherwise
    """
    return isinstance(obj, a_class)
