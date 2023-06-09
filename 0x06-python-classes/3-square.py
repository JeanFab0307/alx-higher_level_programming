#!/usr/bin/python3
"""This module is dedicated to the creation of a Square class
"""


class Square:
    """Create a square with a given size

    Text

    Args:
    __size(int): the size of the square

    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method to calculate the area of a Square

        Return:
            int: The area of the square
        """
        return self.__size ** 2
