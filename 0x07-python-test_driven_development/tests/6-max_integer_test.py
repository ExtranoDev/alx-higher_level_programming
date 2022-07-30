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

    
    def test_result(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([4, 5, 6]), 6)
        self.assertAlmostEqual(max_integer([2, 3, 9, 5, 6]), 9)
        self.assertAlmostEqual(max_integer([12, 8, 3]), 12)
        self.assertAlmostEqual(max_integer([4, -5, 6]), 6)
        self.assertAlmostEqual(max_integer([-2, -3, 8, 67, 0]), 67)
        self.assertAlmostEqual(max_integer([-4, -5, -6]), -4)
        self.assertAlmostEqual(max_integer([6]), 6)
        self.assertAlmostEqual(max_integer([3, 3, 3, 3]), 3)

