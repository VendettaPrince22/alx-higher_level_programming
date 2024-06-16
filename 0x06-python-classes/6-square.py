#!/usr/bin/python3
"""Defines an object square"""


class Square:
    """Defines a class for a square object
    Arguments:
        size (int): width and height of a square; private attribute
        position (tuple): coordinate of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class with size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size attribute"""
        return self.__size

    @property
    def position(self):
        """Retrieves the position attribute"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position attribute"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of a square"""
        return self.size * self.size

    def my_print(self):
        """Prints a square in stdout with # at specified offset"""
        if self.size == 0:
            print("")
        else:
            if self.position[1] > 0:
                for k in range(self.position[1]):
                    print("")
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
