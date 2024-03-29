#!/usr/bin/python3
"""Class Student"""


class Student():
    """Defines a student
Args:
    first_name(str): The first name
    last_name(str): The last name
    age(int): the age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a student"""
        return vars(self)
