#!/usr/bin/python3
"""Contains the `say_my_name` function"""


def say_my_name(first_name, last_name=""):
    """Prints first and last name
    Args:
        first_name (str): the first name
        last_name (str): the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
