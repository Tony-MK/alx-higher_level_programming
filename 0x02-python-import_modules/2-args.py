#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print(n_args, "arguments.")

    else:
        print(n_args, "arguments:\n" + "\n".join([
            "{}: {}".format(index + 1, arg)
            for index, arg in enumerate(sys.argv[1:])
        ]))
