#!/usr/bin/python3
"""this module is for fectching a  specific url"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as response:
        decoded_resp = response.text
        print("Body response:")
        print(f"    - type: {type(decoded_resp)}")
        print(f"    - content: {response}")
