#!/usr/bin/python3
"""
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validator(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    def update(self, *args, **kwargs):
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
        temp_dict = {}
        temp_dict["size"] = self.size
        temp_dict["x"] = self.x
        temp_dict["y"] = self.y
        temp_dict["id"] = self.id
        return temp_dict
