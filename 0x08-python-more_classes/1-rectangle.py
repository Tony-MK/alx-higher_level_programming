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
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("width must be an integer")
        elif value < 0: 
            raise ValueError("width must be >= 0")
        self.__width = int(value)
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int) or isinstance(value, float)): 
            raise TypeError("height must be an integer")
        elif value < 0: 
            raise ValueError("height must be >= 0")
        self.__height = int(value)
