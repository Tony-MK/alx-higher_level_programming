#!/usr/bin/python3
"""
This is the "Rectangle" module
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Object constructor"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return informal string"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.width
            ] * self.height)

    def __repr__(self):
        """Return formal string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
