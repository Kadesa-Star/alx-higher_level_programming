#!/bin/bash
# Sends a request to a URL and displays the status code of the response

url="$1"
curl -s -o /dev/null -w "%{http_code}" "$url"
