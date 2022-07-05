#!/usr/bin/python3
"""
"read_file" function module
"""


def read_file(filename=""):
    """Reads the contents of a file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(end="{:s}".format(line))
