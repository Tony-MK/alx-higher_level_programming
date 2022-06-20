#!/usr/bin/python3

def safe_print_division(a, b):
    y = None
    try:
        y = a/b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(y))
