#!/usr/bin/python3
"""
Square printer

Prints a square pattern with #
"""


def print_square(size):
    """
    Prints square pattern

    Args:
        size (int): length and breadth of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be greater than zero
    """

    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
