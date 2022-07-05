#!/usr/bin/python3
"""
"load_from_json_file" function module
"""
import json


def load_from_json_file(filename):
    """Loads a json object from a file"""
    with open(filename, "r") as f:
        return json.load(f)
