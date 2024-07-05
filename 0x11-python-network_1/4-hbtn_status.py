#!/usr/bin/python3
"""4-hbtn_status
fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
