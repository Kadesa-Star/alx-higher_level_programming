#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = set()

    for element in my_list:
        if isinstance(element, int):
            uniq_ints.add(element)
    result = sum(uniq_ints)
    return (result)
