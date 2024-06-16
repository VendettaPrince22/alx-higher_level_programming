#!/usr/bin/python3
"""Defines an object Square"""


class Square:
    """Defines a class Square
    Arguments:
        size (int): width and height of a square object
    """
    def __init__(self, size=0):
        """Initializes the class"""
        self.size = size

    @property
    def size(self):
        """Gets the property size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the property size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.size * self.size

    def my_print(self):
        """Prints a square onto stdout using character #"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
