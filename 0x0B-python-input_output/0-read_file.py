#!/usr/bin/python3
"""
File reader
"""


def read_file(filename=""):
    """
    Function to Read files

    Args:
        filename (file): filename
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
