#!/usr/bin/python3
"""
Test Module
"""
import unittest
from models.base import Base


class TestingBase(unittest.TestCase):
    """
    """
    def test_attr(self):
        temp = Base()
        #self.assertTrue(hasattr(temp, "nb_objects"))
        #self.assertTrue(hasattr(Base(), "__nb_objects"))
        self.assertTrue(hasattr(temp, "id"))
        self.assertEqual(temp.id, 1)
