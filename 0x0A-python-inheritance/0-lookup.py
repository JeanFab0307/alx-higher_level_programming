#!/usr/bin/python3
"""
This module has the function lookup
"""


def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object

Arg:
    obj: an object
    """
    return list(dir(obj))
