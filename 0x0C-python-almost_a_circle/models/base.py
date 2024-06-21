#!/usr/bin/python3
"""Contains class Base which will be base for others"""


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class Base"""
        if id != None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
