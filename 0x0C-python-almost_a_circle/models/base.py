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
        """
        Validates values in inherited classes

        Args:
            value (int): value 1
            nvalue (str): value identity
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(nvalue))
        if value <= 0 and nvalue in ("height", "width"):
            raise ValueError("{} must be > 0".format(nvalue))
        if value < 0 and nvalue in ("x", "y"):
            raise ValueError("{} must be >= 0".format(nvalue))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Creates a json format of a dictionary

        Args:
            list_dictionaries (dict): dictionary details

        Returns:
            json format of dictionary details
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves objects to file in json format
        
        Args:
            cls (class): class
            list_objs (list): list of instances
        """
        temp_dict = []
        if list_objs is not None:
            temp_dict = [i.to_dictionary() for i in list_objs]
        nm = cls.__name__ + ".json"
        
        with open(nm, 'w') as f:
            f.write(cls.to_json_string(temp_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts json str to python object

        Args:
            json_string (json): json object

        Returns:
            None if json string is None or python
            object format of json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dum_cls = cls(1, 1)
        dum_cls.update(**dictionary)
        return dum_cls
