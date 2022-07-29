#!/usr/bin/python3
# add_integer.py
"""
Adds two Integer
Makes sure the imputs are either int of Float
Enforces an Integer output
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
