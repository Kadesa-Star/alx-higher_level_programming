#!/usr/bin/python3
"""
Uses Basic Authentication with GitHub username and pat to fetch user ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    auth = HTTPBasicAuth(username, token)
    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=auth)
        print(response.json().get('id'))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
