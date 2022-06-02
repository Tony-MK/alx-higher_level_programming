#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    import sys
    sys.path.append(".")
    import calculator_1 as cal
    ops = [("add", '+'), ("sub", "-"), ("mul", "*"), ("div", "/")]
    for attr, op in ops:
        print("{} {} {} = {}".format(a, op, b, getattr(cal, attr)(a, b)))
