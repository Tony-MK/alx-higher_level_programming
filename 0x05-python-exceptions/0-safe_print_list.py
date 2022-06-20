#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for index in range(x):
        try:
            print(end="{}".format(my_list[index]))
            n += 1
        except Exception as e:
            break
    print()
    return n
