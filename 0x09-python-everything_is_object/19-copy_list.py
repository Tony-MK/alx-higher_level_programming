#!/usr/bin/python3
def copy_list(l):
    return type(l)((copy_list(e) if hasattr(e, "__iter__") else e for e in l))
