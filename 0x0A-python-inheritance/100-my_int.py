#!/usr/bin/python3
"""
Defining a class MyInt"
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        if self != other:
            return not super().__eq__(other)
        else:
            return not super().__ne__(other)
