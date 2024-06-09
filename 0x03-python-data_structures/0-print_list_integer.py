#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers

    Args:
        my_list: list with the integers
    """
    for num in my_list:
        print("{:d}".format(num))
