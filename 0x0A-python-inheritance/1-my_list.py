#!/usr/bin/python3
"""
My_LIST module
"""


class MyList(list):
    """
    Represents my list
    """
    def print_sorted(self):
        """Print elements in ascending order"""
        print(list(sorted(self)))
