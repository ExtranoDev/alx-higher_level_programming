#!/usr/bin/python3
"""
Write an object to a text file in JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes object to a textfile
    Using a JSON represention

    Args:
        my_obj (list, dict): first object
        filename (str): name of file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
