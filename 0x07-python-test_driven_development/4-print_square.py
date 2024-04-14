#!/usr/bin/python3
"""this module is for a function that prints squares"""


def print_square(size):
    """prints a square with the character #.
    Args:
        @size: is the size lenght of the square and it must be an int.
    Raises:
        TypeError: if it was not int.
        ValueError: if it is less than a zero."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("test/4-print_square.txt")
