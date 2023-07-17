#!/usr/bin/python3
"""
Contains the function print_square
"""


def print_square(size):
    """
print square using '#'

Example:
    print_square(2)
    ##
    ##

Args:
    size(int): a number >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
        return

    for i in range(size):
        print("#" * size)
