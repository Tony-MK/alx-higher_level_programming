#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for index in range(len(row)-1):
            print(end="{:d} ".format(row[index]))
        print(":d".format(row[index]))
