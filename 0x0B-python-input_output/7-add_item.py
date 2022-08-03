#!/usr/bin/python3
"""
Add items to a python list in a JSON file
"""
import sys, os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

def add_args_pylist(filename):
    """
    Add args to the python file

    Args:
        filename (str): name of the file
    """
    temp_list = []
    if os.path.exists(filename):
        temp_list = load_from_json_file(filename)
    temp_list += sys.argv[1:]
    save_to_json_file(temp_list, filename)

add_args_pylist("add_item.json")
