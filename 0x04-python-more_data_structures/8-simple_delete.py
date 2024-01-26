#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not isinstance(key, str):
        raise TypeError("Key must be a string")

    if key in a_dictionary:
        del a_dictionary[key]
