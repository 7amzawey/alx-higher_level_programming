#!/usr/bin/python3
"""
this module is for appending function
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        """ this function appends a string at the end of a text file.
        Args:
            @filename: is the filename.
            @text: is the text that will be added to the file
        Returns:
            the Appended file
        """
        return (file.write(text))
