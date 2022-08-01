#!/usr/bin/python3
"""
Module checks if objects are of same instance
or inherited (direclty of indiresctly)
"""


def inherits_from(obj, a_class):
    """
    Check if args are of same instance directly or indireclty

    Args:
        obj (object): object
        a_class (object): object

    Returns:
        True if same instance and False otherwise
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
