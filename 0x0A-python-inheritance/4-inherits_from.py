#!/usr/bin/python3
"""Contains the `inherits_from` function"""


def inherits_from(obj, a_class):
    """Checks if object inherits from specific class
    Args:
        obj: what to check
        a_class: class to compare with
    Returns:
        bool; True if it is, False otherwise
    """
    return issubclass(type(obj), a_class)
