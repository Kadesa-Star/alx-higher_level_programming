#!/usr/bin/python3
""" java script object notation"""


import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
