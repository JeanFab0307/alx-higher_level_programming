#!/usr/bin/python3
"""Contain function load_from_json_file"""


from json import loads


def load_from_json_file(filename):
    """Create an object from a JSON file
Arg:
    filenma(str): the pathname of the file which contains the JSON rep
Return:
    The object represented by the JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return loads(f.read())
