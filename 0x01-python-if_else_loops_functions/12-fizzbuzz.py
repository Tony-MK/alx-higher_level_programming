#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(end="Fizz")
        if i % 5 == 0:
            print(end="Buzz")
        elif i % 3 != 0:
            print(end="{}".format(i))
        print(end=" ")
