#!/usr/bin/python3
"""
this module adds a new attribute to an object if it's possible
"""


def add_attribute(obj, attr, val):
    """Add a new attribute to an object if possible.
    Args:
        @obj: the object
        @attr: is the attribute
        @value: is the value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added
        """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
