#!/usr/bin/python3
"""
write a function that creates an object from a "json file"
"""

import json


def load_from_json_file(filename):
    """this function loads from a json file.
    Args:
        @filename: is the file name
    Returns: the created file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
