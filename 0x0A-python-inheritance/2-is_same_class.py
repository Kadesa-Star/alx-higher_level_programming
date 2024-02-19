#!/usr/bin/python3
"""this function returns the type of an object"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class

    Args:
    - obj: the object to check
    - a_class: the class to compare against

    Returns: True if the object is exactly an instance of the specified class
    """

    return (type(obj) == a_class)
