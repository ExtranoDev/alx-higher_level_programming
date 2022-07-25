#!/usr/bin/python3
"""
Creates class and gives it a private attribute
"""


class square:
    """A class with a private attribute

    Attributes:
        size (int): size of square
    """
    def __init__(self, size):
        self.__size = size
