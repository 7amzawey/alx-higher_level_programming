#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instatiation(self):
        """test base instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)
    
    def test_contructor_args(self):
        """test constructor signature with 2 notaself args."""
        with self.assertRaises(TypeError) as error:
            Base.__init__(self, 1, 2)
        msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(error.exception), msg)

    def test_constructor_args_2(self):
        """test constructor with no args"""
        with self.assertRaises(TypeError) as error:
            Base.__init__()
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), msg)

    def test_id(self):
        """test id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)
    def test_id_is_int(self):
        """tests custom int id."""
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_2(self):
        """tests id passed as keyword arg."""
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)
