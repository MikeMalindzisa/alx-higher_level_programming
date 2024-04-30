#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    api_endpoint = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(api_endpoint,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))i
