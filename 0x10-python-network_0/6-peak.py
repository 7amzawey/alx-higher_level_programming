#!/usr/bin/python3
"""
this module is for a function the finds a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """this function fids the peak of list of unsorted ints
    Args:
        list of integers: the list
    Returns:
         the peak
    """
    if len(list_of_integers) == 0:
        return (None)

    sorted_list = sorted(list_of_integers)
    length = len(list_of_integers)
    return sorted_list[length - 1]
