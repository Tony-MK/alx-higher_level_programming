#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    # Finding the maximum linearly
    maximum = my_list[0]
    for n in my_list[1:]:
        if n > maximum:
            maximum = n
    return maximum
