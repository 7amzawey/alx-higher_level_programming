#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrievs the size.
        Returns:
           The the size.
        """
        return self.__size

    @Square.setter
    def size(self, value):
        """Setting the size.
        Args:
            value: the new value of the size.
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
