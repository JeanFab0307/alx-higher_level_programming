#!/usr/bin/python3
"""
Contain the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
returns True if the object is an instance of a class that inherited from
or the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
