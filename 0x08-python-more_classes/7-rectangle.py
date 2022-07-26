#!/usr/bin/python3
"""
Defines a rectangle with more properties
"""


class Rectangle:
    """
    Rectangle class with args width and height

    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (str): Symbol to be printed during print funct call
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the object

        Attributes:
            width (int): width of a rectangle object
            height (int): height of a rectangle object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Prints # in provide rectangle format

        Returns:
            # pattern according to format
            '' if any of the parameter is 0
        """
        str_1 = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                str_1 += (str(self.print_symbol) * self.__width)
                if i is not self.__height - 1:
                    str_1 += "\n"
        return str_1

    def __repr__(self):
        """
        Prints a representation of class

        Returns:
            Appropriate representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes class objects
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
