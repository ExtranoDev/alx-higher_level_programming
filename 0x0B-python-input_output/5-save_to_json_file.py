#!/usr/bin/python3
"""
Write an object to a text file in JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
