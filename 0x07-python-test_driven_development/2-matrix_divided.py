#!/usr/bin/python3
"""
a function to divide a matrix
by a single divisor
"""


def matrix_divided(matrix, div):
    """divide a matrix by an integer rounded to two decimal places"""

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or matrix == []:
        raise TypeError(err_msg)
    row_len = []
    count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_msg)
        row_len.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err_msg)
        count += 1
    if len(set(row_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
