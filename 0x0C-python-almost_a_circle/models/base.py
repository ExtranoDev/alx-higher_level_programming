#!/usr/bin/python3
"""
Module for Base class definition
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing the Bse class

        Args:
            id (int): unique value
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def validator(value, nvalue):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(nvalue))
        if value <= 0 and nvalue in ("height", "width"):
            raise ValueError("{} must be > 0".format(nvalue))
        if value < 0 and nvalue in ("x", "y"):
            raise ValueError("{} must be >= 0".format(nvalue))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None and type(list_objs) is list:
            if not any(issubclass(type(i), cls) for i in list_objs):
                raise TypeError("")
        nm = str(type(list_objs[0]).__name__) + ".json"
        temp_dict = [i.to_dictionary() for i in list_objs]
        with open(nm, 'w') as f:
            f.write(cls.to_json_string(temp_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dum_cls = cls(1, 1)
        dum_cls.update(**dictionary)
        return dum_cls
