#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Consturctor
           Args:
               size: the size of the square.
               position: the position.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves it
        Returns:
           The position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set teh position
           Args:
               value: the is the value to set
           Raises:
                 TypeError: if not a tuple of 2 integers
        """
        if not (isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number > 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            j: is a bloody variable as well.w
            k: another goddam variable.
        """
        for k in range(0, self.__position[1]):
            print("")
        for j in range(0, self.__size):
            for m in range(0, self.__position[0]):
                print(" ", end="")
            for i in range(0, self.__size):
                print("#", end="")
            print()
        if (self.__size == 0):
            print()
