#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ te tests"""
    def test_integers(self):
        """Tests a list of integers"""
        self.assertEqual(max_integer([2, 4, 9, 0]), 9)
        self.assertEqual(max_integer([2, 4, -9, 0]), 4)
        self.assertEqual(max_integer([9, 4, 2, 0]), 9)
        self.assertEqual(max_integer([0, 2, 4, 9]), 9)
        self.assertEqual(max_integer([0, -2, -4, -9]), 0)

    def test_single_int(self):
        """tests a single int value"""
        self.assertEqual(max_integer([8]), 8)

    def test_floats(self):
        """Tests floating point value """
        self.assertEqual(max_integer([2.1, 0.45, 3.0, 1.99, 3.87]), 3.87)
        self.assertEqual(max_integer([2.1, 0.45, 3.0, 1.99, -3.87]), 3.0)
        self.assertEqual(max_integer([-2.1, -0.45, -3.0, -1.99, -3.87]), -0.45)
    
    def test_list_strings(self):
        """ Tests a list of strings"""
        self.assertEqual(max_integer(["Hello", "hey", "hi"]), "hi")

    def test_a_string(self):
        """Tests a list containing one string"""
        self.assertEqual(max_integer("hello"), 'o')
    def test_no_args(self):
        """tests a list with no elements"""
        self.assertEqual(max_integer(), None)

    if __name__=='__main__':
        unittest.main()
