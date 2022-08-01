#!/usr/bin/python3
"""
Module checks if objects are of same instance
"""


def is_kind_of_class(obj, a_class):
    """
    Check if args are of same instance

    Args:
        obj (object): object
        a_class (object): object

    Returns:
        True if same instance and False otherwise
    """
    return isinstance(obj, a_class)
