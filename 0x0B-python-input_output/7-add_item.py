#!/usr/bin/python3
"""
Program for saving a list of json safe objects
to file called add_item.json
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError as e:
        items = []

    finally:
        for item in sys.argv[1:]:
            items.append(item)

        save_to_json_file(items, "add_item.json")
