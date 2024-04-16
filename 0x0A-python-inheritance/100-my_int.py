#!/usr/bin/python3
"""
Defining a class MyInt"
"""
class MyInt(int):
    """My Int Class checks the value of an int"""
    def __eq__(self, other):
        if self != other:
            return not super().__eq__(other)
        else:
            return not super().__ne__(other)
