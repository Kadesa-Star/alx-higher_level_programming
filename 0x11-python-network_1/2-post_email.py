#!/usr/bin/python3
"""
Sends a POST request to a URL with an email
parameter and displays the decoded body of
the response. Uses urllib and sys packages only.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]   # Assuming the URL is provided asfirst arg
    email = sys.argv[2]  # Assuming the email is  as second arg
    # Encode the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    # Create a request object with the POST method and the encoded data
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
