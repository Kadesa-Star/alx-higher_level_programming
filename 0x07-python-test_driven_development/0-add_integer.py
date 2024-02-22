#!/usr/bin/python3
"""this is a function that adds two integers"""


def add_integer(a, b=98):
    """ Adds two integers
    float argurments are typecasted to integers before addition
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
