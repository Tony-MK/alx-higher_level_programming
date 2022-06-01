#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(end="Fizz")
        elif i % 5 == 0:
            print(end="Buzz")
        else:
            print(end="{}".format(i))
        print(end=" ")
