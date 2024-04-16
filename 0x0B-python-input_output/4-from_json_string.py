#!/usr/bin/python3
"""
module for deseriliazation that will return an object represented by json
"""

import json


def from_json_string(my_str):
    """will unjson the my_str"""
    return (json.loads(my_str))
