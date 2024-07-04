#!/bin/bash
# Sends a POST request to a URL with variables email and subject, and displays the response body.
curl -sL -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
