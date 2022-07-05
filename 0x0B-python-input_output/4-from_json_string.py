#!/usr/bin/python3
"""
"from_json_string" function module
"""
import json


def from_json_string(my_str):
    """Return an object from a JSON string"""
    return json.loads(my_str)
