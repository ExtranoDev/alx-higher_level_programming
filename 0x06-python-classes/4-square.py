#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Class Initialization

        Arguments:
            size (int): square size
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and returns the area of a drone
        """
        return self.__size * self.__size
