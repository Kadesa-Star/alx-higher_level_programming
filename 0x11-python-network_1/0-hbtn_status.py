#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib.
Displays various details of the response body with proper formatting.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        raw_content = response.read()
        content = raw_content.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(raw_content)}")
        print(f"\t- content: {raw_content}")
        print(f"\t- utf8 content: {content}")
