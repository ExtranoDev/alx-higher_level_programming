#!/usr/bin/python3
"""
Lookup Function

Module looksup attributes of an object
"""


def lookup(obj):
    """
    Looks up atributes of an object

    Args:
        obj (object): object

    Returns:
        list of attributes specific to the object
    """
    return dir(obj)
