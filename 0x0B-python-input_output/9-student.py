#!/usr/bin/python3
"""
"Student" class module
"""


class Student:
    """ A class representation for a student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of student attributes"""
        return self.__dict__
