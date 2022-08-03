#!/usr/bin/python3
"""
Returns a dict
"""


def class_to_json(obj):
    """
    Gets a dict from a class
    """
    return obj.__dict__
