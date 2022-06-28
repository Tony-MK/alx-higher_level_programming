#!/usr/bin/python3
"""
This is the "Rectangle" module
"""


class Rectangle:
    """
    A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0: 
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0: 
            raise ValueError("height must be >= 0")
        self.__height = value