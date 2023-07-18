#!/usr/bin/python3
"""
Contain the class Rectangl that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry
    Attributes:
    width(int): the width of the Rectangle
    heigth(int): the height of the Rectangle
    """
    
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("heigth", height)
        self.__width = width
        self.__height = height
