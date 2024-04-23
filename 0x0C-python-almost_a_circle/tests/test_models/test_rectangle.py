#!/usr/bin/python3
"""module for test cases for the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the Base Class"""

    def setUp(self):
        """import module, the Base__nb_objects"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after each test_method"""
        pass

    def test_class(self):
        """test Rectangle class type"""
        self.assertEqual(str(Rectangle),
                "<class 'models.rectangle.Rectangle'>")
    def test_inheritance(self):
        """test Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))
    def test_no_args(self):
        """Test if there is no args"""
        with self.assertRaises(TypeError) as error:
            r = Rectangle()
        msg = "Rectangle.__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(error.exception), msg)

    def test_instantiation(self):
        """Test instantiation"""
        r = Rectangle(29, 11)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        dic = {'_Rectangle__height': 11, '_Rectangle__width': 29, '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, dic)


        with self.assertRaises(TypeError) as error:
            r = Rectangle("1", 1)
        msg = "width must be an integer"
        self.assertEqual(str(error.exception), msg)

        with self.assertRaises(TypeError) as error:
            r = Rectangle(1, "1")
        msg = "height must be an integer"
        self.assertEqual(str(error.exception), msg)

        with self.assertRaises(ValueError) as error:
            r = Rectangle(-1, 1)
        msg = "width must be > 0"
        self.assertEqual(str(error.exception), msg)

        with self.assertRaises(ValueError) as error:
            r = Rectangle(1, -1)
        msg = "height must be > 0"
        self.assertEqual(str(error.exception), msg)
