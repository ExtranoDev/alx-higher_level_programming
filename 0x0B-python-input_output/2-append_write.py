#!/usr/bin/python3
"""
File writer
"""


def append_write(filename="", text=""):
    """
    Function appends to files

    Args:
        filename (file): filename
        text (str): text to be written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
