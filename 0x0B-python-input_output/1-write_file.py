#!/usr/bin/python3
"""
This module is specified for a writing funciton
"""


def write_file(filename="", text=""):
    """this function writes a string to a text file utf-8 and.
    returns the number of chars.
    Args:
        @filename: the filename.
        @text: the text that will be written in the file
    Returns:
         The numbe of chars written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
