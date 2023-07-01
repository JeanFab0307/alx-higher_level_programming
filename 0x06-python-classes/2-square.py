#!/usr/bin/python3
"""Module documentation
"""


class Square:
    '''Create a square with a given size

    Text

    Args:
    __size: the size of the square

    '''

    def __init__(self, __size=0):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
