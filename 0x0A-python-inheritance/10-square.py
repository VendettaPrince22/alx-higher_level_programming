#!/usr/bin/python3
"""Contains the `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square object
    Args:
        size: width and height of square
    """
    def __init__(self, size):
        """Initializes the square with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size
