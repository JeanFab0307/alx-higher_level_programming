#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_max_value(self):
        self.assertEqual(max_integer([2, 4, 3, 8]), 8)
        self.assertEqual(max_integer([9, 4, 3, 7]), 9)
        self.assertEqual(max_integer([1, 9, 4, 3, 7]), 9)
        self.assertEqual(max_integer([9, -19, 7]), 9)
        self.assertEqual(max_integer([-2, -1, -3, -8]), -1)
        self.assertEqual(max_integer([5]), 5)

    def test_no_list(self):
        self.assertIsNone(max_integer([]))
