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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle with the character #"""
        for k in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute,
        Assigns key/value argument to attributes"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.__width = args[1]
        elif len(args) == 3:
            self.__height = args[2]
        elif len(args) == 4:
            self.__x = args[3]
        elif len(args) == 5:
            self.__y = args[4]

        if 'height' in kwargs.keys():
            self.__height = kwargs['height']
        if 'width' in kwargs.keys():
            self.__width = kwargs['width']
        if 'x' in kwargs.keys():
            self.__x = kwargs['x']
        if 'y' in kwargs.keys():
            self.__y = kwargs['y']
        if 'id' in kwargs.keys():
            self.id = kwargs['id']
