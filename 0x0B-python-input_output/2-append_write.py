#!/usr/bin/python3
"""
"append_write" function module
"""


def append_write(filename="", text=""):
    """Append text to an existing file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
