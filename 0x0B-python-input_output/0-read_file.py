#!/usr/bin/python3
"""
"read_file" function module
"""

def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read())
