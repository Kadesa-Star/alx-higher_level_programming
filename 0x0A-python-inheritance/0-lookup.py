#!/usr/bin/python3
""" this function returns a list of available attributes and methods"""


def lookup(obj):
    """
    Returns a list of attributes and methods

    Args:
    - obj: the object whose attributes and methods are to be looked up.

    Returns:
    - A list containing the names of attributes and methods
    """

    return dir(obj)
