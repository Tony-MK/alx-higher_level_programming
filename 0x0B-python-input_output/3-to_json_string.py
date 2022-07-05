#!/usr/bin/python3
"""
"to_json_string" function module
"""
import json


def to_json_string(my_obj):
    """Returns the JSON string of an object"""
    return json.dumps(my_obj)
