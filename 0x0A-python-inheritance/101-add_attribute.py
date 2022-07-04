#!/usr/bin/python3
"""
"MyInt" module
"""


class MyInt(int):
    """
    Represents a rebel integer object
    """
    def __eq__(self, x):
        """Return if is not equal to x """
        return self < x or self > x

    def __ne__(self, x):
        """Return if is equal to x"""
        return not (self < x or self > x)
