#!/usr/bin/python3
"""
Performs the addition operation and two integers or one integer with 98
>> add_integer(1, 1)
2
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b
    """
    if not (type(a) == int or type(a) == float):
        raise ValueError("a must be an integer")
    elif not (type(b) == int or type(b) == float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
