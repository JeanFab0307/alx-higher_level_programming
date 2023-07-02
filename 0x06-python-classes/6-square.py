#!/usr/bin/python3
"""This module is dedicated to the creation of a Square class"""


class Square:
    """Create a square with a given size

    Text

    Args:
    __size(int): the size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """Public instance method to calculate the area of a Square

        Return:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square with #"""
        for i in range(self.__position[1]):
            print()
        if self.__size != 0:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
            return
        print()

    @property
    def size(self):
        """int: the size of the Squre"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the value of the attribute size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """tuple: The position to print the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the value of the attribute position"""
        if len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
