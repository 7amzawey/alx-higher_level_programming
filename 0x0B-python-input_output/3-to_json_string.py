#!/usr/bin/python3
"""
this module module is for a function that returns the JSON representation
of an object
"""


import json


def to_json_string(my_obj):
    """returns the json representation"""
    return (json.dumps(my_obj))
