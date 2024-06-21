#!/usr/bin/python3
"""Contains class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle object
    Args:
        width: rectangle's width
        height: rectangle's height
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class with the parameters"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the value for width attribute"""
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height attribute"""
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x attribute"""
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y attribute"""
        self.__y = value
