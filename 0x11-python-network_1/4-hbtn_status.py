#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests."""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.content)}")
    print(f"\t- content: {response.content.decode('utf-8')}")
    print(f"\t- utf8 content: {response.content.decode('utf-8')}")
