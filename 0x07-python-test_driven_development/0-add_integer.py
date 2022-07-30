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

    Args:
        a (int): first variable
        b (int, optional): second variable with 98 as default value

    Raises:
        TypeError: a and b must be integer (Float allowed)

    Returns:
        int: sum of a and b
    """
    for i, nm in [(a, 'a'), (b, 'b')]:
        if type(i) not in (int, float):
            raise TypeError("{} must be an integer".format(nm))
    return int(a) + int(b)
