#!/usr/bin/python3
"""
defining a class that inherirtes from another
"""


class MyList(list):
    """custome the Classa"""
    def print_sorted(self):
        """public instance method that prints the lest but sorted"""
        print(sorted(self))
