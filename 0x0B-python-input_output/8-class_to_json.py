#!/usr/bin/python3
"""
this module for a function that returns
the dict description with simple data struct
"""


def class_to_json(obj):
    """returns the dict description with simple data sturcture for a json
    of an obj.
    Args:
        @obj: is the object
    Returns: the dict of an obj
    """
    return obj.__dict__
