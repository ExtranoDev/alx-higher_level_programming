#!/usr/bin/python3
"""
Class calculates square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        Initializes the Square function and the Rectangle function
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
