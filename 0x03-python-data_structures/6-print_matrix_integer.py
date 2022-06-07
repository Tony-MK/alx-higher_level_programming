#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    list(map(lambda row: print(" ".join(
            list(map(lambda num: "{}".format(num), row)))),
            matrix
    ))
