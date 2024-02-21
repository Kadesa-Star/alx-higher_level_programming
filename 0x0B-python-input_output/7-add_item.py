#!/usr/bin/python3
""" script that adds all arguments to a Python list"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    # load existing items fromfile if it exists
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    arguments = sys.argv[1:]

    # Add new items to the existing list
    existing_items.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(existing_items, "add_item.json")
