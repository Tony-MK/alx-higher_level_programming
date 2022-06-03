#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    OPS = {'+': cal.add, '-': cal.sub, '*': cal.mul, '/': cal.div}
    ERROR_1 = "Unknown operator. Available operators: +, -, * and /\n"

    if len(sys.argv) != 4:
        print(end="Usage: " + sys.argv[0] + " <a> <operator> <b>\n")
        exit(1)
    elif sys.argv[2] not in OPS:
        print(end=ERROR_1)
        exit(1)
    a: int = int(sys.argv[1])
    b: int = int(sys.argv[3])
    op: str = sys.argv[2]
    print("{:d} {} {:d} = {}".format(a, op, b, OPS[op](a, b)))
