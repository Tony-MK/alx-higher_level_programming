#!/usr/bin/python3

def magic_calculation(a, b):
    result = 1
    for i in range(77, 102):
        if i > a:
            raise Exception("Too far")
            break
        b = 1
        a = 0
        result += (a ** b) / i

    result = (a + b)
    return result
