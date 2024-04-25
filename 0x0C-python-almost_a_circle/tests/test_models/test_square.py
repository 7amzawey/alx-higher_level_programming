#!/usr/bin/python3
"""this module for square tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testsquare(unittest.TestCase):
    """this class is for unittesting the square class"""
    def SetUp(self):
        Base._Base__nb_objects = 0
        pass

    def TearDown(self):
        pass
    
    def test_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_inheritance(self):
        """test if square inherits Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_constructor_no_args(self):
        """Tests constructor_no_args"""
        with self.assertRaises(TypeError) as error:
            r = Square()
        s = "Square.__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(error.exception), s)

    def test_instatiation(self):
        """test instantiontion"""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {
            '_Rectangle__height': 10,
            '_Rectangle__width': 10,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0,
            'id': 6
            }
        self.assertEqual(r.__dict__, d)
