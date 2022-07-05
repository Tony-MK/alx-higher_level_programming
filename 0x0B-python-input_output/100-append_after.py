#!/usr/bin/python3
"""
"append_after" function module
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends new string given the line has the search string to a file"""
    data = ""
    with open(filename, "r") as f:
        for line in f:
            data += line
            if search_string in line:
                data += new_string
                print(data)

    with open(filename, "w") as f:
        f.write(data)
