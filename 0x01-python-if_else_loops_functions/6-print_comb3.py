#!/usr/bin/python3
print(", ".join([
    "{}{}".format(n, i)
    for n in range(0, 10) for i in range(n + 1, 10)
    ])
)
