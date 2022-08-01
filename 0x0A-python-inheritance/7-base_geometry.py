#!/usr/bin/python3
"""
Module defines a BaseGeometry class
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer and greater then 0

        Args:
            name (str): str value
            value (int): int value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
