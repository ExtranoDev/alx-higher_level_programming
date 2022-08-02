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

        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
