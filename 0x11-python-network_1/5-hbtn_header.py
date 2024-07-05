#!/usr/bin/python3
"""this module is for printing a header"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers['X-Request-Id'])
