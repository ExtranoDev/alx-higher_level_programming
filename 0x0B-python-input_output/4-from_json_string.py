#!/usr/bin/python3
"""
JSON rep returner
"""
import json


def from_json_string(my_str):
    """
    Converts JSON representation to string

    Args:
        my_str (str): objects

    Returns:
        JSON representation of the inputed object
    """
    return json.loads(my_str)
