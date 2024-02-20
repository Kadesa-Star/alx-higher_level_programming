#!/usr/bin/python3
""" java script object notation"""


import json


def to_json_string(my_obj):
    """Return the JSON representation of the given object"""
    return json.dumps(my_obj)
