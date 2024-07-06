#!/usr/bin/python3
"""we are gonna take my github credentials and use the GITHUB API to display my
id my password will be the PAT"""


if __name__ == '__main__':
    """display my id using the PAT as a password
    Args:
        username: the 1st argument
        password: the 2nd argument"""
    import requests
    import sys

    headers = {
            "Authorization": f"Bearer {sys.argv[2]}",
            "Accept": "application/vnd.github+json"
            }
    response = requests.get(
            f"https://api.github.com/user/{sys.argv[1]}", headers=headers)
    json_response = response.json()
    print(f"{json_response.get('id')}")
