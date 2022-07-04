#!/usr/bin/python3
"""
"BaseGeometry" module
"""


class BaseGeometry:
    """
    A base class to construct a geomertic shape
    """
    def area(self):
        """Return the area of the shape"""
        raise Exception("area() is not implemented")
