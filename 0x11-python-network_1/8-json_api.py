#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000
/search_user with a letter as a parameter.
Handles response to display id and name if
JSON is properly formatted and not empty.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        response = requests.post(url, data={'q': q})
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'],
                  json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print("Error:", e)
