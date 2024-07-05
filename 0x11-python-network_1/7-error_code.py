#!/usr/bin/python3
"""this module is for printing a header"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
