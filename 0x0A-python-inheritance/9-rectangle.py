#!/usr/bin/python3
"""
Module defines a BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Accepts sides mesurements of a rectangle

    Args:
        BaseGeometry (class): inherits class
    """
    def __init__(self, width, height):
        """
        Initialixation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Overwrites the default print method
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
