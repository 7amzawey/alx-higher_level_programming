#!/usr/bin/python3
"""
write a function that creates an object from a "json file"
"""

import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
