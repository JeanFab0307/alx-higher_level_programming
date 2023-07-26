#!/usr/bin/python3
"""Contain function to_json_string"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
Arg:
    my_obj: an object
Return:
    A str of the JSON rep of my_obj
    """
    return json.dumps(my_obj)
