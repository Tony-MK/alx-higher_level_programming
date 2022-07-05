#!/usr/bin/python3
"""
"save_to_json_file" function module
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a json object to a file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
