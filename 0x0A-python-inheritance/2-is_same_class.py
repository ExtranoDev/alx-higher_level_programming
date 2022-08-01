#!/usr/bin/python3
"""
Module checks if objects are of same instance
"""


def is_same_class(obj, a_class):
    """
    Check if args are of same instance

    Args:
        obj (object): object
        a_class (object): object

    Returns:
        True if same instance and False otherwise
    """
    return type(obj) == a_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
