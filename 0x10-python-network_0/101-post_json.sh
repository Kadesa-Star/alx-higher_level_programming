#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Assign arguments to variables for readability
URL=$1
FILE=$2

# Send a POST request with the contents of the file
curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$URL"
