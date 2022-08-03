#!/usr/bin/python3
"""
A Student class file
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization method

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): integer value
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns details of a class instace in a dictionary form
        """
        if attrs is not None and type(attrs) is list:
            temp_dict = dict()
            for i in attrs:
                if i in self.__dict__.keys():
                    temp_dict[i] = self.__dict__.get(i)
            return temp_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Load files like json
        """
        for i in json:
            if i in ['first_name', 'last_name', 'age']:
                self.i = json[i]
