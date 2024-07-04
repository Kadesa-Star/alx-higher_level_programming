#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl, and displays the size of the response body in bytes.

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Save the URL from the command line argument
URL=$1

# Use curl to send a request to the URL and measure the size of the response body
SIZE=$(curl -s "$URL" | wc -c)

# Print the size of the body in bytes
echo "$SIZE"
