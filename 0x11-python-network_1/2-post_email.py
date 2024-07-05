#!/usr/bin/python3
"""this module is for sending a post request to a url with the email as a p"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    encoded_data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data, method='POST')

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
