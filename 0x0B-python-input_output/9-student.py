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

    def to_json(self):
        """
        Returns details of a class instace in a dictionary form
        """
        return self.__dict__
