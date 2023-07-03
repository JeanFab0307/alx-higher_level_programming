#!/usr/bin/python3
"""
This module is reserved for the creation of the class Rectangle.
It contains everything we need about a rectangle object.
"""


class Rectangle:
    """This class is about a rectangle, a four-side shape

Argument:
    number_of_instances(int): the num of rectangle created

    This rectangle has a width and a height that are private to it.

Args:
    heigth(int): the height of the rectangle(0 by default)
    width(int): the width of the rect(0 by default)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        shape = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                if i != 0:
                    shape += "\n"
                shape += "#" * self.__width
        return shape

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Return the width of the object"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of The rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Return the height of the object"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of The rectangle"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
