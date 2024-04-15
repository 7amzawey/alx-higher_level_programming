#!/usr/bin/python3
"""
Defining an object
"""


def lookup(obj):
    """returns the list of available attributes"
    Args:
        @obj: the obj
    Returns: the list of attributes
    """
    return (dir(obj))
