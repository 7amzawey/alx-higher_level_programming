#!/usr/bin/python3
"""Module for add_integer Method"""

def add_integer(a, b=98):
    """Adds 2 intgers.

    Args:
        a: the first integer.
        b: the 2nd integer.

    Raises:
        TypeError: if a and b are not integers or floats.

    Returns:
        an integer result of the addition of the both ints.

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt") 
