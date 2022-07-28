#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Class Initialization

        Arguments:
            size (int): square size
            position (tuple): positional arguements
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
                or not isinstance(value[0], int) or\
                not isinstance(value[1], int) or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and returns the area of a drone
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints pattern when called
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
