#!/usr/bin/python3
"""Contain funtion save_to_json_file"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """Writes an object tp a text file, using a JSON representation
Args:
    my_obj: an object
    filename(str): the pathname of the file where to write the JSON rep
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
