#!/usr/bin/python3
"""the module for a function that process input and then print metrics"""


from sys import stdin


status_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
        }
file_size = i = 0


def printer():
    """this function prints the statistics"""
    print(f'File_size: {file_size}')
    for key, value in sorted(status_code.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        splitted_line = line.split()
        if len(splitted_line) >= 2:
            file_size += int(splitted_line[-1])
            status = splitted_line[-2]
        if status in status_code:
            status_code[status] += 1
        i += 1

    if i % 10 == 0:
        printer()

    printer()
except KeyboardInterrupt:
    printer()
