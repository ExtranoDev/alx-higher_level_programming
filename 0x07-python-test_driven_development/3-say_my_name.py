#!/usr/bin/python3
"""
Name Printer

Prints supplied name in an assorted format
"""


def say_my_name(first_name, last_name=""):
    """
    Prints supplies name

    Args:
        first_name (str): first arg
        last_name (str. optional): second arg

    Raises:
        TypeError: arguements must be type str
    """

    for nm, nms in ((first_name, "first_name"), (last_name, "last_name")):
        if not isinstance(nm, str):
            raise TypeError("{} must be a string".format(nms))
    print("My name is {} {}".format(first_name, last_name))
