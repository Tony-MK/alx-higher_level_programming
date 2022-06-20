#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print(end="{:d}".format(my_list[i]))
            n += 1
        except (TypeError, ValueError) as e:
            pass
    print(end="\n")
    return n
