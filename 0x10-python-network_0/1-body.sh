#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body of the response (only for a 200 status code response).

response=$(curl -s -w "%{http_code}" -o /dev/null "$1")

if [[ $response == 200* ]]; then
    curl -s "$1"
fi
