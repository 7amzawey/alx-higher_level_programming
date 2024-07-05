#!/usr/bin/python3
"""this module is for fetching a specific URL"""


if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    decoded_resp = response.text
    print("Body response:")
    print(f"    - type: {type(decoded_resp)}")
    print(f"    - content: {decoded_resp}")
