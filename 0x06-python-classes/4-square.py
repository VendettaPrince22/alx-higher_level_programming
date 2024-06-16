#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square object
    Arguments:
        size (int): height and width of a square; private instance
    """

    def __init__(self, size=0):
        """Initializes the class square with size"""
        self.size = size

        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.size * self.size
