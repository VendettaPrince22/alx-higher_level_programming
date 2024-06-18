#!/usr/bin/python3
"""Contains the class `MyList` inheriting from `list`"""


class MyList(list):
    """Defines a class MyList derived from class list"""

    def print_sorted(self):
        """Prints the list, but sorted"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
