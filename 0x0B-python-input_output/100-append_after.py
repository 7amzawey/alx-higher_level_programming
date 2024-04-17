#!/usr/bin/python3
"""
this module is for a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a lone of text to a file, after each line
    containgin a specific word.
    """
    with open(filename, 'r') as file:
        lines_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            lines_list.append(line)
            if search_string in line:
                lines_list.append(new_string)
    with open(filename, 'w') as file:
        file.writelines(lines_list)
