#!/usr/bin/python3
"""
Sends a request to a URL and displays the decoded body of the response.
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
Uses urllib and sys packages only.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Assuming the URL is provided as the first argument
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
