#!/usr/bin/python3
def uppercase(s: str):
    print("".join([
        chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        for c in s
    ]), end="{}".format("\n"))
