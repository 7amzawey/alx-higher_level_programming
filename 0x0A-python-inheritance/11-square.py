#!/usr/bin/python3
"""Defining a rectangle Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
