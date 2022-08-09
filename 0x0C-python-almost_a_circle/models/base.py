#!/usr/bin/python3
"""
Module for Base class definition
"""
import json
import csv


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
        """
        Creates a new class instance from a dictionary

        Args:
            cls (class): class
            dictionary (dict): a dictionary of instances

        Returns:
            a class instance created using a dictionary
        """
        dum_cls = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dum_cls.update(**dictionary)
        return dum_cls

    @classmethod
    def load_from_file(cls):
        """
        Load json string from a file

        Args:
            cls (class): object class

        Returns:
            a python list object
        """
        nm = cls.__name__ + ".json"
        try:
            with open(nm, 'r') as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**i) for i in dict_list]
        except Exception:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Load class attributes from csv

        Args:
            cls (class): class instance

        Returns:
            empty list if file is empty of
            list of instance of a class
        """
        nm = cls.__name__ + ".csv"
        try:
            with open(nm, 'r') as f:
                fld_name = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    del fld_name[1:3]
                    fld_name.insert(1, "size")
                csv_r = csv.DictReader(f, fieldnames=fld_name)
                list_objs = [dict([k, int(v)] for k, v in dt.items())
                             for dt in csv_r]
            return [cls.create(**i) for i in list_objs]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save details of class in csv

        Args:
            cls (class): class instance
            list_objs (list): list of class instance
        """
        nm = cls.__name__ + ".csv"
        with open(nm, "w") as f:
            if list_objs is not None and list_objs != []:
                list_dict = [i.to_dictionary() for i in list_objs]

                fld_name = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    del fld_name[1:3]
                    fld_name.insert(1, "size")

                writer = csv.DictWriter(f, fieldnames=fld_name)
                for i in list_dict:
                    writer.writerow(i)
            else:
                f.write("[]")
