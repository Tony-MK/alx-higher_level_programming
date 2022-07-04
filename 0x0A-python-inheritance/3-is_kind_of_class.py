#!/usr/bin/python3
"""
"is_kind_of_class" module
"""


def is_kind_of_class(obj, a_class):
    """Return if the object is an instance of class or derived"""
    if type(obj) == a_class or issubclass(obj, a_class):
        return True
    return isinstance(obj, a_class)
