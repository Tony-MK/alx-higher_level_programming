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

    print(" ".join(list(map(str, sys.argv[1:]))), end=" = ")
    print(OPERATORS[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
