#!/usr/bin/python3
"""
Matrix Divider

Divides a Matrix by a given divisor
"""


def matrix_divided(matrix, div):
    """
    Divides Matrix

    Args:
        matrix (list): matrix of the format [[1, 2, 3], [4, 5, 6]]
        div (int): Divideer

    Raises:
        TypeError: matrix must be type list of list and
                    and elements of matrix must be integer of float
        TypeError: Each row in matrice must be of same size
        TypeError: divider must be a number
        ZeroDivisionError: division by zero error

    Returns:
        list: new matrix already divided
    """

    if type(matrix) == list and matrix != []:
        for vals in matrix:
            if type(vals) == list:
                if all(type(i) in (int, float) for i in vals):
                    continue
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(matrix[0]) == len(i) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in nm] for nm in matrix]
