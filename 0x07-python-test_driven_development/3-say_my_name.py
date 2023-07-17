#!/usr/bin/python3
"""
This module contains the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>

Args:
    first_name(str): no initial value
    last_name(str): initialized to ""

    Args ust be strings or a error is raise
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    last = ""
    if last_name != "":
        last = " " + last_name
    print("My name is {}{}".format(first_name, last))
