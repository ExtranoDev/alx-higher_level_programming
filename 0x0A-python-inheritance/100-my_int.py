#!/usr/bin/python3
"""
Defines Int class
"""


class MyInt(int):
    """
    Int class
    """

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
