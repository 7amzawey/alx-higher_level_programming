#!/usr/bin/python3
"""
this module is for a function that will return a list of lists of integers representing
the pascal triangle of n
"""


def pascal_triangle(n):
    """this function will return a list of lists of integers.
    @Args:
        @n: is the number that the pascal triangle will represent.
    Returns: a list of lists of integers
    """
    if n <= 0:
        return []
    
    # [ nCm = (n-1)C(m-1) + (n-1)Cm ]
    # n: the row number
    # m : the position within the row.
    for sl in bl:
        for e in sl:
            sl[e] = b1[bl.index[sl] - 1] [s1.index[e] - 1] + bl[b1.index[sl] -1] [s1.index[s1]] 
    return (bl)
