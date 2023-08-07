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

    def to_json(self, attr=None):
        """Retrieves a dict representation of a student"""
        if attr is None or type(attr) is not list:
            return vars(self)
        else:
            result = {}
            for item in attr:
                if item == 'age':
                    result[item] = self.age
                if item == 'first_name':
                    result[item] = self.first_name
                if item == 'last_name':
                    result[item] = self.last_name
            return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        self.first_name= json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
