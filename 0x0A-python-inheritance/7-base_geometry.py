#!/usr/bin/python3
"""
You can find the class BaseGeometry and all its methods here
"""


class BaseGeometry:
    """
    The shape of certain elements
    """

    def area(self):
        """
        Raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
    Args:
        name(str): the name of the shape
        value(int): to see later
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
