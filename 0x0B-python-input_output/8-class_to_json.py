#!/usr/bin/python3
"""
"clas_to_json" function module
"""


def class_to_json(obj):
    """Returns a dictionary of attributes from an object"""
    return obj.__dict__
