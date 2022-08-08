#!/usr/bin/python3
"""
Modules for create a square version of the Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class

    Args:
        Rectangle (class): inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of the Square class

        Args:
            size (int): square dimension
            x (int): printer position 1
            y (int): printer position 2
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Dimension of Square

        Returns:
            the value of the size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.validator(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Format printing for the class Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the values in Square

        Args:
            args (list): atrr of class square
            kwargs (dict): dictionary of attrr
        """
        if len(args) == 0:
            if "size" in kwargs.keys():
                temp = kwargs.pop("size")
                kwargs["height"] = temp
                kwargs["width"] = temp
            super().update(**kwargs)
        else:
            if len(args) >= 2:
                temp = args[1]
                args = list(args)
                args.insert(1, temp)
            super().update(*args)

    def to_dictionary(self):
        """
        Converts attrbutes in class as dictionary
        """
        temp_dict = {}
        temp_dict["size"] = self.size
        temp_dict["x"] = self.x
        temp_dict["y"] = self.y
        temp_dict["id"] = self.id
        return temp_dict
