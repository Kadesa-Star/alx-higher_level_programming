#!/usr/bin/python3
""" java script object notation"""


import json


def from_json_string(my_str):
    """Return the Python data structure represented by JSON string"""
    return json.loads(my_str)
