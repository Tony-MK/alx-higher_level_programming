#!/usr/bin/python3
"""
class Square - A class that defines a square
"""


class Square:
    """Class for a square object"""
    def __init__(self, size=0):
        self.size = size

    def area(self) -> int:
        """Compute area of the square object"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints square object to STDOUT """
        print("\n".join(["#" * self.size] * self.size))
