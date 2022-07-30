#!/usr/bin/python3
"""Unittest for max_integer

Tester for max_integer file
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Texter Class

    Args:
        unittest.TestCase (unnittest): inherit something
    """

    
    #def test_islist(self):
        #self.assertRaises(TypeError, max_integer, {})
        #self.assertRaises(TypeError, max_integer, "School")
        #self.assertRaises(TypeError, max_integer, None)

    def test_result(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([4, 5, 6]), 6)
