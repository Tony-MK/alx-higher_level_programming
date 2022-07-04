#!/usr/bin/python3
"""
"inherits_from" module
"""


def inherits_from(obj, a_class):
    """Return if the object is inherited from the class"""
    return isinstance(obj, a_class) or issubclass(obj, a_class)
