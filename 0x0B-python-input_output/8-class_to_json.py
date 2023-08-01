#!/usr/bin/python3
"""Function class_to_obj(obj)"""
from json import dumps


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return dumps(obj.__dict__)
