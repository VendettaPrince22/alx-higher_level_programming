#!/usr/bin/python3
"""Conteins a class Rectangle"""


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

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        """Prints a rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""

        string_list = []
        for i in range(self.height):
            for j in range(self.width):
                string_list.append("#")
            if i != self.height - 1:
                string_list.append("\n")

        string = "".join(string_list)

        return string
