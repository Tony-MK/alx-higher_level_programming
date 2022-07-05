#!/usr/bin/python3
"""
"read_file" function module
"""

def read_file(filename=""):
    with open(filename, "r", "UTF-8") as f:
        for l in f:
            print(l)
