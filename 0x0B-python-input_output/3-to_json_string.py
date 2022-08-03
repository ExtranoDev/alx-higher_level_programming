#!/usr/bin/python3
"""
"""
import json


def to_json_string(my_obj):
    """
    Converts objects to JSON representation

    Args:
        my_obj (list, dict): objects

    Returns:
        JSON representation of the inputed object
    """
    return json.dumps(my_obj)
