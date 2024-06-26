#!/usr/bin/python3
"""
Defining an empty class called Rectangle
"""


class Rectangle:
    """defination of the rectangle class.
    """
    def __init__(self, width=0, height=0):
        """initilization of the width and height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property getter for the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """property Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """property Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
