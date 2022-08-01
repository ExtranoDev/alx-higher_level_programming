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
