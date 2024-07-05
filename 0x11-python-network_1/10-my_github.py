#!/usr/bin/python3
"""
Uses Basic Authentication with a GitHub personal access token to fetch user ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./github_id.py <username> <token>")
        sys.exit(1)
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
