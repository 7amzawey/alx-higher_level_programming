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

    @size.setter
    def size(self, value):
        """Setting the size.
        Args:
            value: the new value of the size.
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square.

           Returns:
               The size squared
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the bloody square.
        Args:
            i: is a bloody variable
            j: is a bloody variable as well.
        """
        for j in range(0, self.__size):
            for i in range(0, self.__size):
                print("#", end="")
            print()
        if (self.__size == 0):
            print()
