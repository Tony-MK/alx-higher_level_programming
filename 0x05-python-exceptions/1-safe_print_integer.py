#!/usr/bin/bash
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        return False
