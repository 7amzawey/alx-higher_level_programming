#!/usr/bin/python3
"""this module is for printing a header"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        print(response.text)

    except requests.exceptions.HTTPError as e:  # Corrected to `requests.exceptions.HTTPError`
        print(f"Error code: {e.response.status_code}")  # Corrected `e.response.stauts_code` to `e.response.status_code`
