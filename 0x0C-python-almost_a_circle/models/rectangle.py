#!/usr/bin/python3
"""
Module defines a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base class

    Args:
        Base (class): inherits Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing the Ractangle calss

        Args:
            width (int): size 1
            height (int): size 2
            x (int): arg 1
            y (int): arg 2

        Raises:
            TypeError: when arguement is not an integer
            ValueError: when unaccepted arg is passed
        """

        for val, nval in [(width, "width"), (height, "height"),
                          (x, "x"), (y, "y")]:
            self.validator(val, nval)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Function format for print
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    @property
    def width(self):
        """
        Width getter

        Returns:
            the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.validator(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Height getter

        Returns:
            the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.validator(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        X getter

        Returns:
            the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.validator(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Y getter

        Returns:
            the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.validator(value, "y")
        self.__y = value

    def area(self):
        """
        Returns Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Creates a format for displaying patters
        """
        height = self.__height
        x = self.x
        y = self.y

        for i in range(y):
            print("")

        while height != 0:
            print(" " * x + "#" * self.__width)
            height -= 1

    def update(self, *args, **kwargs):
        """
        Updates instance attributes

        Args:
            args (list): list of attributes
            kwargs (dict): dictionary format of attributes
        """
        if len(args) == 0:
            for i in kwargs.keys():
                if i == "id":
                    self.id = kwargs[i]
                elif i == "width":
                    self.width = kwargs[i]
                elif i == "height":
                    self.height = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
        else:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """
        Creates a dictionary format of all attributes
        """
        temp_dict = {}
        temp_dict["width"] = self.width
        temp_dict["height"] = self.height
        temp_dict["x"] = self.x
        temp_dict["y"] = self.y
        temp_dict["id"] = self.id
        return temp_dict
