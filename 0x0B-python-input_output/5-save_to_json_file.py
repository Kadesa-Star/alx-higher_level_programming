#!/usr/bin/python3
""" java script object notation"""


import json


def save_to_json_file(my_obj, filename):
    """object to a text file using its JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
