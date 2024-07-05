#!/usr/bin/python3
"""
Sends a POST request with email as parameter to a given URL using requests.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
