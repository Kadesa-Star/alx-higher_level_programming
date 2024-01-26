#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dele = [key for key, val in a_dictionary.items() if val == value]

    for key in dele:
        del a_dictionary[key]
