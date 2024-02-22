#/usr/bin/python3
"""module to find the maximum int in a list"""

def max_integer(list=[]):
    """function to find max int in a list of ints
    if list is empty, function returns none """
    if len(list) == 0:
        return None
    result = list(0)
    l = 1
    while l < len(list):
        if list[l] > result:
            result = list[l]
        l += 1
    return result
