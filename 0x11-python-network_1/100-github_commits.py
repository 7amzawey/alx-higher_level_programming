#!/usr/bin/python3

"""
Listing the 10 last commits from most recent to oldest.
"""

import requests
import sys

if __name__ == '__main__':

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    params = {'per_page': 10}
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url, params=params)
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
