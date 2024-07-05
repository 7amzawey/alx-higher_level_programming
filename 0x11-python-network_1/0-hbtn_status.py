#!/usr/bin/python3
"""this module is for fectching a  specific url"""

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        resp = response.read()
        decoded_resp = resp.decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(resp)}")
        print(f"    - content: {resp}")
        print(f"    - utf8 content: {decoded_resp}")
