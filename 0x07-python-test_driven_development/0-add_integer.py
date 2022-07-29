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
    values = []
    for i, nm in [(a, 'a'), (b, 'b')]:
        if not isinstance(i, int):
            if not isinstance(i, float):
                raise TypeError("{} must be an integer".format(nm))
            else:
                values.append(int(i))
        else:
            values.append(i)
    return sum(values)
