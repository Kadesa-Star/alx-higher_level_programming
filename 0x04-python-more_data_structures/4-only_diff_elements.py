#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # combine the two sets to get unique elements
    all_uniq = set_1.union(set_2)

    # calculate the symmetric
    only_diff = set_1.symmetric_difference(set_2)

    return (only_diff)
