#!/usr/bin/python3
"""
class Square - A class that defines a square
"""


class Square:
    """Class for a square object"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(value, tuple) and len(value) == 2 and
            isinstance(value[0], int) and value[0] >= 0 and
            isinstance(value[1], int) and value[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints square object to STDOUT """
        print(("\n" * self.position[1] + "\n".join([
            " " * self.position[0] + "#" * self.size
            ] * self.size)) if self.size > 0 else ""
        )
