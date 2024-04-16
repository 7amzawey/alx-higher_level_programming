#!/usr/bin/python3
"""
this module is for appending function
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        """ this function appends a string at the end of a text file"""
        return (file.write(text))
