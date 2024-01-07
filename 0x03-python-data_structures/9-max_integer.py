#!/usr/bin/python3
def max_integer(my_list=[]):
    sort = sorted(my_list)
    length = len(my_list)
    if length == 0:
        return "None"
    else:
        return (sort[length - 1])
