#!usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    l_a, l_b = len(tuple_a), len(tuple_b)
    return tuple(
            (0 if l_a <= i else tuple_a[i]) + (0 if l_b <= i else tuple_b[i])
            for i in range(2)
            )
