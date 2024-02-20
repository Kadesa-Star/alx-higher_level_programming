#!/usr/bin/python3
""" script that adds all arguments to a Python list"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


# get args excluding script name
arguments = sys.argv[1:]

# load existing items fromfile if it exists
try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

# Add new items to the existing list
existing_items.extend(arguments)

# Save the updated list to the file
save_to_json_file(existing_items, "add_item.json")
