#!/usr/bin/python3
"""
Line Indenter and Printer

Prints new Line after an encounter with some string literals
"""


def text_indentation(text):
    """
    Prints text with blank lines

    Args:
        text (str): text to be printed

    Raises:
        TypeError: when text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    
    txt = ""
    for i in text:
        txt += i
        if i in ".?:":
            print(txt.strip() + "\n")
            txt = ""

    if txt != "":
        print(txt.strip(), end="")
