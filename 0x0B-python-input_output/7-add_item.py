#!/usr/bin/python3
"""
this module is for a script that adds all arguments a python list,
and save them to a file
"""

import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    data = load('add_item.json')
except Exception:
    data = []

data.extend(args)
save(data, 'add_item.json')
