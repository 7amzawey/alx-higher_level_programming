#!/usr/bin/python3
"""
this module is for a function that reads a text file
"""


def read_file(filename=""):
    """this function reads a text file"""
    with open(filename, encoding='utf-8') as file:
        """Read the content of the file into a string"""
        print(file.read(), end="")
