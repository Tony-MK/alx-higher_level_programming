#!/usr/bin/python3
def print_last_digit(number):
    digit: int = abs(number) % 10
    print(end=f"{digit}")
    return digit
