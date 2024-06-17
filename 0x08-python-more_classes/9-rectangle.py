#!/usr/bin/python3
"""Contains a class Rectangle"""


class Rectangle:
    """Defines a rectangle object
    Args:
        width: the width of a rectangle
        height: the height of a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class with a width and haight"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                string_list.append(str(self.print_symbol))
            if i != self.height - 1:
                string_list.append("\n")

        string = "".join(string_list)

        return string

    def __repr__(self):
        """String representation of the rectangle object created"""
        return str("Rectangle("+str(self.width)+", "+str(self.height)+")")

    def __del__(self):
        """Deletes a Rectangle object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        if rect_2_area > rect_1_area:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
