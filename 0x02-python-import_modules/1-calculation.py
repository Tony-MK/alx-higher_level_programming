#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    module = __import__("calculator_1")
    ops = [("add", '+'), ("sub", "-"), ("mul", "*"), ("div", "/")]
    for attr, op in ops:
        print("{} {} {} = {}".format(a, op, b, getattr(module, attr)(a, b)))
