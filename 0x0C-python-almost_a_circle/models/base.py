#!/usr/bin/python3
"""Base class"""


class Base():
    """Base of the other class(parentclass)
Attr:
    __nb_objects(int): the number of instances created
Arg:
    id(int): the id of the object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id
            
