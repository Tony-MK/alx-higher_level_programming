#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str = 'zero' if number == 0 else ('positive' if number > 0 else 'negative')
print(f'{number:d} is {str}')
