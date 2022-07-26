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
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            self.__width = value
        except ValueError:
            print("width must be >= 0")
        except TypeError:
            print("width must be an integer")

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
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            self.__height = value
        except ValueError:
            print("height must be >= 0")
        except TypeError:
            print("height must be an integer")
