#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    """
    """
    if type(matrix) == list and matrix != []:
        for vals in matrix:
            if type(vals) == list:
                if all(type(i) in (int, float) for i in vals):
                    continue
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    if not all(len(matrix[0]) == len(i) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not any([isinstance(div, i) for i in (int, float)]):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in nm] for nm in matrix]
