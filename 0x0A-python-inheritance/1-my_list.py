#!/usr/bin/python3
"""
Contains MyList that inherits from list
"""


class MyList(list):
    """
    Inherit the function list
    """

    def print_sorted(self):
        """
        Prints a sorted list
        """
        tmp = self[:]
        super().sort()
        print(self)
        self = tmp[:]
