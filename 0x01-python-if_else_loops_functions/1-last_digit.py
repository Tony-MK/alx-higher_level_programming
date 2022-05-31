#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(abs(number) % 10)
if last_digit == 0:
    str = '0'
else:
    str = ('greater than 5' if number > 5 else 'less than 6')
print(f'Last digit of {number} is {last_digit} and is {str}')
