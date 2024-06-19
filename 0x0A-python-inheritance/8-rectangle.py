#!/usr/bin/python3
"""Contains the `Rectangle` class that inherits from `BaseGeometry`"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle with width and height
    Args:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width, height):
        """Initializes a Rectangle object with width & height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
