#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a square
    Args:
        size (int): width and height of a square; private instance
    """

    def __init__(self, size=0):
        """Initializes the class square with size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
