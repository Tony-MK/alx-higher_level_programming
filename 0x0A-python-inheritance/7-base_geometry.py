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

    def integer_validator(self, name, value):
        """Validates whether value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
