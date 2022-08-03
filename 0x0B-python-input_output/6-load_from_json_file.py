#!/usr/bin/python3
"""
A python object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates a python object from a JSON file

    Args:
        filename (str): name of file
    """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.readline())
