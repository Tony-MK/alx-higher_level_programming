#!/usr/bin/python3
if __name__ == "__main__":
    add = __import__("add_0").add
    print("{} + {} = {}".format(1, 2, add(1, 2)))
