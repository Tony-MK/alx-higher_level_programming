#!/usr/bin/python3
for c in range(97, 123):
    if c != 101 and str(chr(c)) != 'q':
        print(end="{}".format(chr(c)))
