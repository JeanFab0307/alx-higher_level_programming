#!/usr/bin/python3
"""
This module contains the function add_integer.
"""


def add_integer(a, b=98):
    """
This function adds two int and return their sum.

Args:
    a(int): first number
    b(int): second number initialized to 98

Return:
    a+b
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
