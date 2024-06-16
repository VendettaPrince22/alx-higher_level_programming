#!/usr/bin/python3
"""Holds only one function / method - add_integer
    Args:
        a (int): first parameter
        b (int): second parameter
"""


def add_integer(a, b=98):
    """Adds 2 integers
    Returns: sum of a and b (int)
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
