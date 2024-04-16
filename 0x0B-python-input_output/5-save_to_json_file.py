#!/usr/bin/python3
"""
Module for a function that writes an object to a text file, using a
json representation
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
