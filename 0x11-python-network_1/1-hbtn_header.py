#!/usr/bin/python3
"""this module is for printing a header"""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
