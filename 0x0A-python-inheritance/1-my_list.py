#!/usr/bin/python3
"""
List Sorter
"""


class MyList(list):
    """
    Class takes a list object as parent class

    Args:
        list (object): list object
    """

    def print_sorted(self):
        """
        Prints sorted a copy of the instance list
        """
        print(sorted(self))
