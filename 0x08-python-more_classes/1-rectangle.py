#!/usr/bin/python3
"""
This module is reserved for the creation of the class Rectangle.
It contains everything we need about a rectangle object.
"""


class Rectangle:
    """This class is about a rectangle, a four-side shape

    This rectangle has a width and a height that are private to it.

Args:
    heigth(int): the height of the rectangle(0 by default)
    width(int): the width of the rect(0 by default)
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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
