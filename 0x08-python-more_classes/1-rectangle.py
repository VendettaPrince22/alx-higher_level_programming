#!/usr/bin/python3
"""Holds a class rectangle"""


class Rectangle:
    """Defines a rectangle object
    Args:
        width: the width of a rectangle
        height: the height of a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the class with a width and haight"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the attribute width"""
        return self.__width

    @property
    def height(self):
        """Retrieves the attribute height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets a value for the width attribute (private)"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets a value for the height attribute (private)"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
