#!/usr/bin/python3
"""
File writer
"""


def write_file(filename="", text=""):
    """
    Function write to files

    Args:
        filename (file): filename
        text (str): text to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
