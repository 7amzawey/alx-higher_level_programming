#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square.
        Raises:
            ValueError: is the size is less than 0.
            TypeError: if size is not int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square.

           Returns:
               The size squared
        """
        return (self.__size * self.__size)
