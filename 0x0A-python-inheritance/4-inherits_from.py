#!/usr/bin/python3
"""
A module fro iherits_from method
"""


def inherits_from(obj, a_class):
    """check if obj is a subclass"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
