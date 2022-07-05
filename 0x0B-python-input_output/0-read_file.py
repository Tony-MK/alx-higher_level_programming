#!/usr/bin/python3
"""
"read_file" function module
"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read())
