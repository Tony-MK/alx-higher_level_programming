#!/usr/bin/python3
def copy_list(l):
    return type(l)((copy_list(e) if type(e) in [dict, list, set] else e for e in l))
