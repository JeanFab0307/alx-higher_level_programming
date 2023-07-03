#!/usr/bin/python3
"""This module is dedicated to the creation of a Square class"""


class Square:
    """Create a square with a given size

    Text

    Args:
    __size(int): the size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Public instance method to calculate the area of a Square

        Return:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square with #"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
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
        messErr = "position must be a tuple of 2 positive integers"
        if type(position) != tuple or len(position) != 2:
            raise TypeError(messErr)
        for i in range(len(position)):
            if type(position[i]) != int or position[i] < 0:
                raise TypeError(messErr)
        self.__position = position
