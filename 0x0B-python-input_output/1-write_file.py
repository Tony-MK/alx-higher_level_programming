#!/usr/bin/python3
"""
"write_file" function module
"""


def write_file(filename="", text=""):
    """Writes data to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
