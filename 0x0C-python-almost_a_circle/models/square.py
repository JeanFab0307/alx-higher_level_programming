#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """class Square
Args:
    size(int): the size of the square
    x(int): position on x axis(x=0)
    y(int): position on y axis (y=0)
    id(int): the id(id=None)
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
