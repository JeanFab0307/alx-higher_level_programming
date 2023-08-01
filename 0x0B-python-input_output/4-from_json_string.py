#!/usr/bin/python3
"""Function from_json_string(str)"""
from json import loads


def from_json_string(my_str):
    """Return and Object represented by a JSON string"""
    return loads(my_str)
