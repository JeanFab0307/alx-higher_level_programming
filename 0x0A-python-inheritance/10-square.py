#!/usr/bin/python3
"""Contain the class Square that inherits for Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class
Attributes:
    size(int): the size of the square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
