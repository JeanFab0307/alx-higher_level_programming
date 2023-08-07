#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from class base
Args:
    __width(int): the width of the rect
    __height(int): the height of the rect
    __x(int): the position of the rect on the x axis
    __y(int): the position of the rect on the y axis
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x 
