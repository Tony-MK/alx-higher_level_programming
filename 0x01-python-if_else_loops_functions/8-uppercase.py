#!/usr/bin/python3
def uppercase(s: str):
    for c in s:
        o = ord(c)
        print(end=chr(o - 32) if o >= 97 and o <= 122 else c)
    print(end="\n")
