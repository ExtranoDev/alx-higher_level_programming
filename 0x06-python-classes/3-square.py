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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and returns the area of a drone
        """
        return self.__size * self.__size
