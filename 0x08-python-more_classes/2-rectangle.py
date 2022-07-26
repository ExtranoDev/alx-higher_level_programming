#!/usr/bin/python3
"""
Defines a rectangle with more properties
"""


class Rectangle:
    """
    Rectangle class with args width and height

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        int: width property of the rectangle

        Checks if width is an Integer and makes sure it's less
        greater than zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: height property of rectangle

        Checks if height is an integer and makes sure it's less
        than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of rectangle w*l

        Returns:
            Area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of rectangle

        Returns:
            Perimeter of rectangle
            And 0 if any of width or length is 0
        """
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        return 0
