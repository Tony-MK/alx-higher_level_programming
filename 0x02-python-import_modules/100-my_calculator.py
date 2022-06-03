#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    OPERATORS = {'+': cal.add, '-': cal.sub, '*': cal.mul, '/': cal.div}
    ERROR_1 = "Unknown operator. Available operators: +, -, * and /\n"

    if len(sys.argv) != 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    elif sys.argv[2] not in OPERATORS:
        sys.stderr.write(ERROR_1)
        sys.exit(1)
    a: int = int(sys.argv[1])
    b: int = int(sys.argv[3])
    print("{:d} {} {:d}".format(a, sys.argv[2], b), end=" = ")
    print(OPERATORS[sys.argv[2]](a, b))
