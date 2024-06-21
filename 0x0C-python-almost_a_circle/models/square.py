#!/usr/bin/python3
"""Contains the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object with size
    Args:
        size: width and height of the square
        x: offset x
        y: offset y
        id: id number
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """Overloading representation for square object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
