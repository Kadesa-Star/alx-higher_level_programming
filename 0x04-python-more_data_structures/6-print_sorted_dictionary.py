#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # alist of sorted keys
    sort_key = sorted(a_dictionary.keys())

    # move throught the sorted keys and print key valude pairs
    for key in sort_key:
        value = a_dictionary[key]

        if isinstance(vallue, dict):
            print(f"{key}:")
            print_sorted_dictionary(value)
        else:
            print(f"{key}: {value}")
