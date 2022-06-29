#!/usr/bin/python3
"""
Divides a matrix with a number
"""


def martix_divided(matrix, div):
    """
    Return the division of a matrix and a number
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    elif type(int) != type(div) and type(div) != type(int):
        raise TypeError("")
    y = []
    for r in matrix:
        if not isintance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(y) != 0 and len(y[0]) != len(r):
            raise TypeError("Each row of the matrix must have the same size")
        y.append([n/div for in r])
    return y
