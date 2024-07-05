#!/usr/bin/python3
"""
Fetches a URL provided as an argument, sends a request, and displays the value
of the X-Request-Id variable found in the response header using urllib and sys.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Assuming the URL is provided as the first argument
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
