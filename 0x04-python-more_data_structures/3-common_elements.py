#!/usr/bin/python3
def common_elements(set_1, set_2):
    # initialize empty set to store common elements
    comm = set()

    for element in set_1:
        if element in set_2:
            comm.add(element)

    return (comm)
