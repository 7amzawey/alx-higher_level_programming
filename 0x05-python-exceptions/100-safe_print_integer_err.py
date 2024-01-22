#!/usr/bin/python3
import sys
is_int = True
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        is_int = False
    return is_int          
