#!usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    l_a, l_b = len(tuple_a), len(tuple_b)
    return (
            (0 if l_a <= 0 else tuple_a[0]) + (0 if l_b <= 0 else tuple_b[0]),
            (0 if l_a <= 1 else tuple_a[1]) + (0 if l_b <= 1 else tuple_b[1])
            )
