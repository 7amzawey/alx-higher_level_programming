#!/usr/bin/python3
"""this module is for sending a post request to a url with the email as a p"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
